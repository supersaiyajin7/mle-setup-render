import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.parametrize(
    "payload, expected_status",
    [
        ({"text": "I love it!"}, 200),
        ({"text": ""}, 400),
    ],
)

def test_sentiment_prediction(payload, expected_status):
    response = client.post("/sentiment/predict", json=payload)
    assert response.status_code == expected_status

    if expected_status == 200:
        data = response.json()
        assert "label" in data
        assert "score" in data
