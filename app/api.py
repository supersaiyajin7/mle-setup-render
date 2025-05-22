# app/api.py

from fastapi import APIRouter, HTTPException
from app.schemas import SentimentRequest, SentimentResponse
from app.model import SentimentModel

router = APIRouter()
model = SentimentModel()

@router.post("/predict", response_model=SentimentResponse)
def predict_sentiment(data: SentimentRequest):
    try:
        result = model.predict(data.text)
        return SentimentResponse(**result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
