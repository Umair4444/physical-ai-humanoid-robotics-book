from fastapi import APIRouter, Depends, HTTPException, status
from typing import Dict, Any, Optional
from uuid import UUID
from pydantic import BaseModel

from ..services.rag_service import RAGService
from ..models.rag_log import RAGQueryMode

router = APIRouter()

class RAGQueryRequest(BaseModel):
    query: str
    mode: RAGQueryMode
    selected_text: Optional[str] = None
    user_id: Optional[UUID] = None # Placeholder for actual user authentication

@router.post("/rag/query", response_model=Dict[str, Any], status_code=status.HTTP_200_OK)
async def query_rag_chatbot(
    request: RAGQueryRequest,
    rag_service: RAGService = Depends(RAGService)
) -> Dict[str, Any]:
    """
    Handles queries to the RAG chatbot.
    """
    try:
        if request.mode == RAGQueryMode.FULL_BOOK:
            response = await rag_service.query_full_book(query=request.query, user_id=request.user_id)
        elif request.mode == RAGQueryMode.SELECTED_TEXT:
            if not request.selected_text:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="'selected_text' is required for 'selected-text' mode."
                )
            response = await rag_service.query_selected_text(
                query=request.query,
                selected_text=request.selected_text,
                user_id=request.user_id
            )
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid RAG query mode.")

        return response
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
