from fastapi import APIRouter, UploadFile, File, Form
from typing import List
from api.schemas.response import PitchEvaluateResponse
from api.agent.pitch_evaluation_agent import evaluate_pitch_audio
from api.schemas.request import FillMissingPartsRequest
from api.schemas.request import ScriptEvaluateRequest
from api.schemas.request import SimilarityAnalyzeRequest
from api.schemas.response import FillMissingPartsResponse
from api.schemas.response import ScriptEvaluateResponse
from api.schemas.response import SimilarityAnalyzeResponse
from api.agent.prototype_generator import fill_missing_parts
from api.agent.evaluate_script import evaluate_script
from api.agent.evaluate_material import analyze_similarity
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/pitch-evaluate", response_model=PitchEvaluateResponse)
async def evaluate_pitch(
    file: UploadFile = File(...),
    user_panel_count: int = Form(...)
):
    return await evaluate_pitch_audio(file, user_panel_count)

@router.post("/fill/", response_model=FillMissingPartsResponse)
async def fill_missing(request: FillMissingPartsRequest):
    filled = fill_missing_parts(request.incomplete_text, request.reference_texts)
    return FillMissingPartsResponse(completed_text=filled)

@router.post("/evaluate-script", response_model=ScriptEvaluateResponse)
async def evaluate_script_api(request: ScriptEvaluateRequest):
    try:
        result = evaluate_script(request.script_text)
        return ScriptEvaluateResponse(
            correct_sentences=result["correct_sentences"],
            incorrect_sentences=result["incorrect_sentences"]
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"스크립트 평가 중 오류 발생: {str(e)}"}
        )
    
@router.post("/analyze-similarity", response_model=SimilarityAnalyzeResponse)
async def analyze_similarity_api(request: SimilarityAnalyzeRequest):
    try:
        result = analyze_similarity(
            file_path=request.file_path,
            vector_db_path=request.vector_db_path,
            top_k=request.top_k
        )
        return SimilarityAnalyzeResponse(
            average_similarity=result["average_similarity"],
            most_similar_sentences=result["most_similar_sentences"],
            least_similar_sentences=result["least_similar_sentences"]
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Error during similarity analysis: {str(e)}"}
        )