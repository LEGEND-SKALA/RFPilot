# main.py
from fastapi import FastAPI
from api.routers.router import router
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware

load_dotenv() #환경 변수 
app = FastAPI(title="RFPilot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # 또는 ["*"] 모든 도메인 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 발표 평가 라우터 등록
app.include_router(router, prefix="/pitch-evaluation", tags=["Pitch Evaluation"])