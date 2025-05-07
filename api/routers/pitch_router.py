from fastapi import APIRouter, UploadFile, File, Form
from typing import List
from api.schemas.pitch import PitchEvaluateResponse
from api.agent.pitch_evaluation_agent import evaluate_pitch_audio

router = APIRouter()

@router.post("/pitch-evaluate", response_model=PitchEvaluateResponse)
async def evaluate_pitch(
    file: UploadFile = File(...),
    user_panel_count: int = Form(...)
):
    return await evaluate_pitch_audio(file, user_panel_count)