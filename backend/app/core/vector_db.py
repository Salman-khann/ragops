"""Vector database service for ChromaDB."""

import chromadb
from app.core.config import settings

# Initialize ChromaDB client
chroma_client = chromadb.HttpClient(
    host=settings.CHROMA_HOST,
    port=settings.CHROMA_PORT
)


def get_collection():
    """Get or create ChromaDB collection."""
    return chroma_client.get_or_create_collection(
        name=settings.CHROMA_COLLECTION
    )


def get_chroma_client():
    """Get ChromaDB client instance."""
    return chroma_client
