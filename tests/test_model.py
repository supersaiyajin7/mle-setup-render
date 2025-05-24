from app.services.model import SentimentModel
import pytest

model = SentimentModel()

def test_model_positive():
    result = model.predict("I love this!")
    assert result["label"] in [
            "1 star", "2 stars", "3 stars", "4 stars", "5 stars"
        ]
    assert 0 <= float(result["score"]) <= 1

def test_model_empty_input():
    with pytest.raises(ValueError):
        model.predict(" ")
