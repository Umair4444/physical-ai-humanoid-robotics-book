from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class ChapterVector(BaseModel):
    """
    Represents a vectorized chunk of book content for storage in Qdrant.
    """
    chapter_id: str = Field(..., description="Identifier for the chapter (e.g., 'module-1-chapter-1-1')")
    text_chunk: str = Field(..., description="The original text segment that was vectorized.")
    embedding: List[float] = Field(..., description="The numerical vector representation of the text chunk.")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Additional metadata like section, page number, etc.")

    class Config:
        schema_extra = {
            "example": {
                "chapter_id": "module-1-chapter-1-1",
                "text_chunk": "This is a text chunk from the book.",
                "embedding": [0.1, 0.2, 0.3, ...], # Example, actual size will vary
                "metadata": {"section": "Introduction", "page": 10}
            }
        }
