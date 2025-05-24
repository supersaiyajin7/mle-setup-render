## FILE: app/services/summarizer.py

from transformers import pipeline

class Summarizer:
    def __init__(self):
        self.pipeline = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

    def summarize(self, text: str) -> str:
        result = self.pipeline(text, max_length=130, min_length=30, do_sample=False)
        return result[0]["summary_text"]
