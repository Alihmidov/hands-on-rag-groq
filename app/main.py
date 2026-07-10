from fastapi import FastAPI 
from app.routes.api import router 

app = FastAPI()  

@router.get("/health_check", summary="Check server status")
def health_check():
    return {"status": "online", "message": "Api is running."}

app.include_router(router)