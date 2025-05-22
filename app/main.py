# app/main.py

from fastapi import FastAPI
from app.api import router

app = FastAPI(title="LLM Sentiment API")

app.include_router(router)
