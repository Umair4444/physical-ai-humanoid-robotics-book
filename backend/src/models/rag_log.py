from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4
from enum import Enum

from pydantic import BaseModel, Field

class RAGQueryMode(str, Enum):
    """
    Defines the mode of the RAG chatbot query.
    """
    FULL_BOOK = "full-book"
    SELECTED_TEXT = "selected-text"

class RAGLog(BaseModel):
    """
    Represents a log entry for a RAG chatbot interaction.
    """
    log_id: UUID = Field(default_factory=uuid4, description="Unique identifier for the log entry.")
    user_id: Optional[UUID] = Field(None, description="References User Profile.user_id if the user is signed in.")
    query_text: str = Field(..., description="The question asked by the user.")
    response_text: str = Field(..., description="The answer provided by the chatbot.")
    source_chapter: Optional[str] = Field(None, description="Reference to the chapter(s) used for the response.")
    source_url: Optional[str] = Field(None, description="URL to the relevant section in the book.")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Timestamp of the query/response.")
    mode: RAGQueryMode = Field(..., description="Query mode - 'full-book' or 'selected-text'.")

    class Config:
        schema_extra = {
            "example": {
                "log_id": "123e4567-e89b-12d3-a456-426614174000",
                "user_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "query_text": "What is physical AI?",
                "response_text": "Physical AI refers to...",
                "source_chapter": "1.1: Introduction to Embodied Intelligence",
                "source_url": "/docs/module-1/chapter-1",
                "timestamp": "2025-12-10T12:00:00.000Z",
                "mode": "full-book"
            }
        }
