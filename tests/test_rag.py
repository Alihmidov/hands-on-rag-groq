import pytest 
from app.core.llm_logic import ask_bot

def test_answer():
    question = "Who is Donald Trump?"
    response = ask_bot(question)
    assert "sorry" in response.lower()