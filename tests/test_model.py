# tests/test_model.py

import pytest
from app.model import SentimentModel

def test_prediction_output_structure():
    model = SentimentModel()
    result = model.predict("I love machine learning!")
    assert "label" in result and "score" in result
    assert result["label"] in {"POSITIVE", "NEGATIVE"}

def test_prediction_empty_input():
    model = SentimentModel()
    with pytest.raises(ValueError):
        model.predict("")
