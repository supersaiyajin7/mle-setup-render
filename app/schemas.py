# app/schemas.py

from pydantic import BaseModel

class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    label: str
    score: str

class SummaryInput(BaseModel):
    text: str

class SummaryOutput(BaseModel):
    summary: str
