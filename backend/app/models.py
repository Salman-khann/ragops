"""Database models."""

from datetime import datetime
from sqlalchemy import Column, String, Text, Float, DateTime, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class AuditLog(Base):
    """Table to audit every interaction for compliance."""
    
    __tablename__ = "audit_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    user_query = Column(Text, nullable=False)
    retrieved_doc_ids = Column(Text)  # Stored as comma-separated string
    generated_response = Column(Text)
    model_used = Column(String, nullable=False)
    execution_time = Column(Float)
    
    def __repr__(self):
        return f"<AuditLog(id={self.id}, timestamp={self.timestamp}, model={self.model_used})>"
