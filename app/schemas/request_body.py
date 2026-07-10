from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    query: str = Field(..., examples = ["What is Machine Learning?",
                                        "What is overfitting?",
                                        "What is the difference between Decision tree and Random Forest?"])