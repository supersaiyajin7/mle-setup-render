from fastapi import FastAPI
from app.api import sentiment, summarize
from app.core.logging import setup_logging

logger = setup_logging()

app = FastAPI()
app.include_router(sentiment.router, prefix="/api")
app.include_router(summarize.router, prefix="/api")

@app.on_event("startup")
def startup_event():
    logger.info("✅ FastAPI app started")
