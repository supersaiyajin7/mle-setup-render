# app/model.py

from transformers import pipeline
from typing import Dict

class SentimentModel:
    def __init__(self, model_name: str = "distilbert-base-uncased-finetuned-sst-2-english"):
        self.pipeline = pipeline("sentiment-analysis", model=model_name)

    def predict(self, text: str) -> Dict[str, str]:
        if not text.strip():
            raise ValueError("Input text is empty")
        result = self.pipeline(text)[0]
        return {
            "label": result["label"],
            "score": f"{result['score']:.4f}"
        }

