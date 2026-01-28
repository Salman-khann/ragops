import os
import uuid
import time
from datetime import datetime
from typing import List, Optional

from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, String, Text, Float, DateTime, Integer
from sqlalchemy.future import select
from minio import Minio
import chromadb
from chromadb.config import Settings
import ollama

MINIO_ENDPOINT = "localhost:9000"
MINIO_ACCESS_KEY = "minioadmin"
MINIO_SECRET_KEY = "minioadmin"
MINIO_BUCKET = "knowledge-base"

CHROMA_HOST = "localhost"
CHROMA_PORT = 8000
DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/ragops"

# --- 1. Database Setup (PostgreSQL) ---
engine = create_async_engine(DATABASE_URL, echo=False)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()


class AuditLog(Base):
    """Table to audit every interaction for compliance."""
    __tablename__ = "audit_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user_query = Column(Text)
    retrieved_doc_ids = Column(Text)  # Stored as comma-separated string
    generated_response = Column(Text)
    model_used = Column(String)
    execution_time = Column(Float)


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


async def init_db():
    """Initialize DB tables on startup."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)



minio_client = Minio(
    MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False
)

if not minio_client.bucket_exists(MINIO_BUCKET):
    minio_client.make_bucket(MINIO_BUCKET)


chroma_client = chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)
collection = chroma_client.get_or_create_collection(name="docs_collection")

class QueryRequest(BaseModel):
    query: str
    model: str = "llama3.2"

class QueryResponse(BaseModel):
    answer: str
    context_sources: List[str]
    audit_id: int

app = FastAPI(title="Local-First RAG Platform")

@app.on_event("startup")
async def on_startup():
    await init_db()
@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """
    1. Uploads file to MinIO.
    2. Extracts text (simple decoding for this demo).
    3. Embeds text into ChromaDB.
    """
    try:
        # A. Upload to MinIO
        file_content = await file.read()
        file_size = len(file_content)
        
        # Reset cursor to beginning for upload
        import io
        file_stream = io.BytesIO(file_content)
        
        minio_client.put_object(
            MINIO_BUCKET,
            file.filename,
            file_stream,
            length=file_size
        )
        text_content = file_content.decode("utf-8")
        doc_id = f"{file.filename}-{uuid.uuid4()}"
        collection.add(
            documents=[text_content],
            metadatas=[{"source": file.filename}],
            ids=[doc_id]
        )
        return {"status": "success", "file": file.filename, "vector_id": doc_id}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/query", response_model=QueryResponse)
async def query_knowledge_base(request: QueryRequest, db: AsyncSession = Depends(get_db)):
    """
    1. Search ChromaDB for relevant context.
    2. Construct prompt for Ollama.
    3. Generate answer.
    4. Log interaction to PostgreSQL.
    """
    start_time = time.time()
    
    # A. Retrieve Context from Chroma
    results = collection.query(
        query_texts=[request.query],
        n_results=3
    )
    if not results['documents'][0]:
        context_text = "No relevant context found."
        retrieved_ids = []
        sources = []
    else:
        context_text = "\n\n".join(results['documents'][0])
        retrieved_ids = results['ids'][0]
        sources = [m['source'] for m in results['metadatas'][0]]

    # B. Construct Prompt
    prompt = f"Using the following context, answer the user's question.\n\nContext: {context_text}\n\nQuestion: {request.query}"
    try:
        response = ollama.chat(model=request.model, messages=[
            {'role': 'user', 'content': prompt},
        ])
        answer_text = response['message']['content']
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Ollama Error: {str(e)}")

    execution_time = time.time() - start_time
    audit_entry = AuditLog(
        user_query=request.query,
        retrieved_doc_ids=",".join(retrieved_ids),
        generated_response=answer_text,
        model_used=request.model,
        execution_time=execution_time
    )
    db.add(audit_entry)
    await db.commit()
    await db.refresh(audit_entry)

    return QueryResponse(
        answer=answer_text,
        context_sources=sources,
        audit_id=audit_entry.id
    )