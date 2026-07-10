from app.schemas.request_body import ChatRequest 
from fastapi import APIRouter
from app.core.llm_model import ask_bot

router = APIRouter()

@router.post("/chat",summary="Ask your questions and get an answer based on document context")
def chat(request: ChatRequest):
    return {"answer": ask_bot(request.query)}