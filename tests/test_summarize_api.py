from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_summarize_success():
    text = "Transformers are models that use attention mechanisms for NLP tasks. They have revolutionized the field."
    response = client.post("/summarize", json={"text": text})
    assert response.status_code == 200
    assert "summary" in response.json()
