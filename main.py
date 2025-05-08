# main.py
from fastapi import FastAPI
from api.routers.chunk_router import router as chunk_router
from api.routers.router import router
from dotenv import load_dotenv
import os

load_dotenv() #환경 변수 
app = FastAPI(title="RFPilot")

app.include_router(chunk_router)
app.include_router(router, prefix="/pitch-evaluation", tags=["Pitch Evaluation"])
