"""Query endpoint for RAG."""

import time
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import ollama

from app.schemas import QueryRequest, QueryResponse
from app.models import AuditLog
from app.core.database import get_db
from app.core.vector_db import get_collection

router = APIRouter()


@router.post("/", response_model=QueryResponse)
async def query_knowledge_base(
    request: QueryRequest,
    db: AsyncSession = Depends(get_db)
):
    """
    Query the knowledge base with RAG.
    
    Steps:
    1. Search ChromaDB for relevant context
    2. Construct prompt for LLM
    3. Generate answer using Ollama
    4. Log interaction to PostgreSQL
    """
    start_time = time.time()
    
    # Retrieve context from ChromaDB
    collection = get_collection()
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
    
    # Construct prompt
    prompt = (
        f"Using the following context, answer the user's question.\n\n"
        f"Context: {context_text}\n\n"
        f"Question: {request.query}"
    )
    
    # Generate answer with Ollama
    try:
        response = ollama.chat(
            model=request.model,
            messages=[{'role': 'user', 'content': prompt}]
        )
        answer_text = response['message']['content']
    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"Ollama Error: {str(e)}"
        )
    
    # Log to database
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
