## FILE: app/schemas/summarize.py

from pydantic import BaseModel

class SummaryInput(BaseModel):
    text: str

class SummaryOutput(BaseModel):
    summary: str
