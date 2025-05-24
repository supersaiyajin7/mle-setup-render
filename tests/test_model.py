from app.services.model import SentimentModel
import pytest

model = SentimentModel()

def test_model_positive():
    result = model.predict("I love this!")
    assert result["label"] in ["POSITIVE", "NEGATIVE"]
    assert 0 <= float(result["score"]) <= 1

def test_model_empty_input():
    with pytest.raises(ValueError):
        model.predict(" ")
