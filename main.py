# main.py
from fastapi import FastAPI
from RFPilot.api.routers.router import router as pitch_router
from dotenv import load_dotenv
import os

load_dotenv() #환경 변수 
app = FastAPI(title="RFPilot")

# 발표 평가 라우터 등록
app.include_router(pitch_router, prefix="/pitch-evaluation", tags=["Pitch Evaluation"])