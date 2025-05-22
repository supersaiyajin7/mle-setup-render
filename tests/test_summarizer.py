from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_summarize():
    payload = {
        "text": "Machine learning is a field of artificial intelligence that uses statistical techniques to give computer systems the ability to learn from data."
    }
    response = client.post("/summarize", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "summary" in data
    assert isinstance(data["summary"], str)
    assert len(data["summary"]) > 0
