# tests/test_api.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_endpoint():
    response = client.post("/predict", json={"text": "This is amazing!"})
    assert response.status_code == 200
    data = response.json()
    assert "label" in data and "score" in data

def test_predict_empty_text():
    response = client.post("/predict", json={"text": ""})
    assert response.status_code == 400
