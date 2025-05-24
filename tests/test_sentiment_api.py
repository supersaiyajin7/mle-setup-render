from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_sentiment_predict_success():
    response = client.post("/sentiment/predict", json={"text": "I love it!"})
    assert response.status_code == 200
    assert "label" in response.json()

def test_sentiment_predict_empty():
    response = client.post("/sentiment/predict", json={"text": ""})
    assert response.status_code == 400
