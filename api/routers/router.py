from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
from typing import List
from api.agent.pitch_evaluation_agent import evaluate_pitch_audio

# from api.agent.prototype_generator import fill_missing_parts
# from api.agent.evaluate_script_agent import evaluate_script
# from api.agent.evaluate_material import analyze_similarity
from api.services.chunking import extract_text_from_file
from api.services.chunking import chunk_text
from api.services.embedding import embed_chunks

from api.agent.summary_agent import summarize_proposal
from api.agent.generate_judges import generate_judges
from api.agent.analysis_fit_agent import analyze_fit
from api.agent.suggest_trends_agent import suggest_trends
import fitz
from api.schemas.response import (
    PitchEvaluateResponse, FillMissingPartsResponse,
    ScriptEvaluateResponse, SimilarityAnalyzeResponse
)
from api.schemas.request import (
    FillMissingPartsRequest, ScriptEvaluateRequest,
    SimilarityAnalyzeRequest
)

router = APIRouter()
async def extract_text_from_file(file):
    contents = await file.read()
    with fitz.open(stream=contents, filetype="pdf") as doc:
        text = "\n".join([page.get_text() for page in doc])
    return text
# ----------------------------
# 🔹 분석(summary) 관련 라우트
# ----------------------------
@router.post("/proposal")
async def analyze_proposal(
    file: UploadFile = File(...),
    company_name: str = Form(...),
    service_description: str = Form(...),
    judge_count: int = Form(...)
):
    # 1. 텍스트 추출
    text = await extract_text_from_file(file)

    # 2. 텍스트 청크 분할 및 임베딩 저장
    chunks = chunk_text(text)
    embed_chunks(chunks, file.filename)

    # 3. 제안서 요약
    summary = summarize_proposal(file.filename)

    # 4. 심사위원 생성
    judges = generate_judges(judge_count, company_name, service_description)

    # 5. 적합도 분석
    score_by_category = analyze_fit(file.filename, top_k=5)

    # 6. 트렌드 제안
    suggestions = suggest_trends(file.filename)

    # 저장할 경로 (예: 현재 폴더에 'example.txt')
    file_path = "judges.txt"

    # 파일에 쓰기
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)
    
    return {
        "summary": summary,
        "judges": judges,
        "fit_score": score_by_category,
        "trend_suggestions": suggestions
    }

# ----------------------------
# 🔹 피치 평가 관련 API
# ----------------------------
@router.post("/pitch-evaluation", response_model=PitchEvaluateResponse)
async def evaluate_pitch(
    file: UploadFile = File(...),
    user_panel_count: int = Form(...),
    doc_title: str = Form(...)
):
    return evaluate_pitch_audio(file, user_panel_count, doc_title)

# @router.post("/pitch-evaluation/fill", response_model=FillMissingPartsResponse)
# async def fill_missing(file: UploadFile = File(...)):
#     filled = fill_missing_parts(file)
#     return FillMissingPartsResponse(completed_text=filled)

# @router.post("/pitch-evaluation/evaluate-script", response_model=ScriptEvaluateResponse)
# async def evaluate_script_api(request: ScriptEvaluateRequest):
#     try:
#         result = evaluate_script(request.script_text)
#         return ScriptEvaluateResponse(
#             correct_sentences=result["correct_sentences"],
#             incorrect_sentences=result["incorrect_sentences"]
#         )
#     except Exception as e:
#         return JSONResponse(
#             status_code=500,
#             content={"error": f"스크립트 평가 중 오류 발생: {str(e)}"}
#         )

# @router.post("/fill/", response_model=FillMissingPartsResponse)
# async def fill_missing(file: UploadFile = File(...)):
#     filled = fill_missing_parts(file)
#     return FillMissingPartsResponse(completed_text=filled)

# @router.post("/evaluate-script", response_model=ScriptEvaluateResponse)
# async def evaluate_script_api(request: ScriptEvaluateRequest):
#     try:
#         result = evaluate_script(request.script_text)
#         return ScriptEvaluateResponse(
#             correct_sentences=result["correct_sentences"],
#             incorrect_sentences=result["incorrect_sentences"]
#         )
#     except Exception as e:
#         return JSONResponse(
#             status_code=500,
#             content={"error": f"스크립트 평가 중 오류 발생: {str(e)}"}
#         )
    
# @router.post("/analyze-similarity", response_model=SimilarityAnalyzeResponse)
# async def analyze_similarity_api(file: UploadFile = File(...)):
#     comment = "시작"
#     try:
#         result = analyze_similarity(
#             file
#         )
#         text = extract_text_from_file(file)
#         comment = "extract완료"
#         evaluatedtext = evaluate_text_by_judges(text)
#         return SimilarityAnalyzeResponse(
#             average_similarity=result["average_similarity"],
#             most_similar_sentences=result["most_similar_sentences"],
#             least_similar_sentences=result["least_similar_sentences"],
#             evaluated_sentences = evaluatedtext,
#         )
#     except Exception as e:
#         return JSONResponse(
#             status_code=500,
#             content={"error": f"Error during similarity analysis: {str(e)},"}
#         )
    