
## FILE: app/api/summarize.py

from fastapi import APIRouter
from app.schemas.summarizer import SummaryInput, SummaryOutput
from app.services.summarizer import Summarizer

router = APIRouter()
summarizer = Summarizer()

@router.post("/summarize", response_model=SummaryOutput)
def summarize_text(data: SummaryInput):
    summary = summarizer.summarize(data.text)
    return SummaryOutput(summary=summary)

