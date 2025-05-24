from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_summarize_success():
    text = "FastAPI is a modern, fast web framework for Python that allows for easy API development."
    response = client.post("/summarize/summarize", json={"text": text})
    assert response.status_code == 200
    assert "summary" in response.json()
