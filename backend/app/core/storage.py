"""Storage service for MinIO."""

from minio import Minio
from app.core.config import settings

# Initialize MinIO client
minio_client = Minio(
    settings.MINIO_ENDPOINT,
    access_key=settings.MINIO_ACCESS_KEY,
    secret_key=settings.MINIO_SECRET_KEY,
    secure=settings.MINIO_SECURE
)


def init_minio():
    """Initialize MinIO bucket."""
    if not minio_client.bucket_exists(settings.MINIO_BUCKET):
        minio_client.make_bucket(settings.MINIO_BUCKET)


def get_minio_client() -> Minio:
    """Get MinIO client instance."""
    return minio_client
