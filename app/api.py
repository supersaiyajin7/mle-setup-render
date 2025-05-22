from fastapi import APIRouter, HTTPException
from app.schemas import SentimentRequest, SentimentResponse
from app.model import SentimentModel

from app.schemas import SummaryInput, SummaryOutput
from app.summarizer import Summarizer

router = APIRouter()
model = SentimentModel()
summarizer = Summarizer() 

@router.post("/predict", response_model=SentimentResponse)
def predict_sentiment(data: SentimentRequest):
    try:
        result = model.predict(data.text)
        return SentimentResponse(**result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/summarize", response_model=SummaryOutput)
def summarize_text(data: SummaryInput):
    summary = summarizer.summarize(data.text)
    return SummaryOutput(summary=summary)
