"""API routes initialization."""

from fastapi import APIRouter
from app.api import upload, query, health

api_router = APIRouter()

api_router.include_router(health.router, tags=["health"])
api_router.include_router(upload.router, prefix="/upload", tags=["upload"])
api_router.include_router(query.router, prefix="/query", tags=["query"])
