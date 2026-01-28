"""File upload endpoint."""

import uuid
import io
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.schemas import UploadResponse
from app.core.storage import get_minio_client
from app.core.vector_db import get_collection
from app.core.config import settings

router = APIRouter()


@router.post("/", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    """
    Upload a document to the knowledge base.
    
    Steps:
    1. Upload file to MinIO
    2. Extract text content
    3. Create embeddings and store in ChromaDB
    """
    try:
        # Read file content
        file_content = await file.read()
        file_size = len(file_content)
        
        # Upload to MinIO
        minio_client = get_minio_client()
        file_stream = io.BytesIO(file_content)
        
        minio_client.put_object(
            settings.MINIO_BUCKET,
            file.filename,
            file_stream,
            length=file_size
        )
        
        # Extract text and add to ChromaDB
        text_content = file_content.decode("utf-8")
        doc_id = f"{file.filename}-{uuid.uuid4()}"
        
        collection = get_collection()
        collection.add(
            documents=[text_content],
            metadatas=[{"source": file.filename}],
            ids=[doc_id]
        )
        
        return UploadResponse(
            status="success",
            file=file.filename,
            vector_id=doc_id
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
