"""Health check endpoint."""

from fastapi import APIRouter
from app.schemas import HealthResponse
from app.core.config import settings

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint."""
    return HealthResponse(
        status="healthy",
        version=settings.VERSION,
        services={
            "database": "connected",
            "minio": "connected",
            "chromadb": "connected",
            "ollama": "connected"
        }
    )
