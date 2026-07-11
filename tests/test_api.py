import pytest 
from fastapi.testclient import TestClient 
from app.main import app 

client = TestClient(app)

def end_point_exists():
    response = client.post("/chat",json = {"query": "Hello"})
    assert response.status_code == 200