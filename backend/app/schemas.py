"""Pydantic schemas for request/response validation."""

from typing import List, Optional
from pydantic import BaseModel, Field


class QueryRequest(BaseModel):
    """Query request schema."""
    
    query: str = Field(..., min_length=1, description="User query")
    model: str = Field(default="llama3.2", description="LLM model to use")


class QueryResponse(BaseModel):
    """Query response schema."""
    
    answer: str = Field(..., description="Generated answer")
    context_sources: List[str] = Field(default=[], description="Source documents")
    audit_id: int = Field(..., description="Audit log entry ID")


class UploadResponse(BaseModel):
    """File upload response schema."""
    
    status: str = Field(..., description="Upload status")
    file: str = Field(..., description="Filename")
    vector_id: str = Field(..., description="Vector database ID")


class HealthResponse(BaseModel):
    """Health check response schema."""
    
    status: str
    version: str
    services: dict
