from pydantic_settings import Basemodel, Field

class ChatRequest(Basemodel):
    query: str = Field(..., examples = ["What is Machine Learning?",
                                        "What is overfitting?",
                                        "What is the difference between Decision tree and Random Forest?"])