from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str
    PROJECT_NAME: str
    EMBEDDING_MODEL: str
    LLM_MODEL: str
    CHROMA_PATH: str
    CHUNK_SIZE: int
    CHUNK_OVERLAP: int
    GROQ_API_KEY: str
    DEBUG: bool
    
    class Config:
        env_file = ".env"

settings = Settings()