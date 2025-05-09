from fastapi import UploadFile
import tempfile, os
from typing import List

import whisper
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter

from api.schemas.response import PitchEvaluateResponse
from api.models.vector_store import load_proposal_vector_db 

def load_whisper_model():
    return whisper.load_model("base")

# 발표 음성 파일을 텍스트로 변환
def transcribe_audio(file: UploadFile) -> str:
    whisper_model = load_whisper_model()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(file.file.read())
        tmp_path = tmp.name
    result = whisper_model.transcribe(tmp_path)
    os.remove(tmp_path)
    return result["text"]

# 심사위원 평가 로직 수행
def run_evaluation(transcript: str, panel_count: int, vector_db) -> List[str]:
    splitter = CharacterTextSplitter(separator="\n", chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(transcript)

    PANEL_ROLES = [
        ("기술 심사위원", "너는 기술 기준으로 발표 내용을 평가하고, 제안서와 비교하여 보완점을 피드백해."),
        ("사업 심사위원", "너는 사업성 관점에서 시장성, 수익성, 전략 등을 평가하는 심사자야."),
        ("실행 심사위원", "너는 실행 가능성과 리스크 측면에서 발표를 검토하는 역할이야.")
    ]

    feedback_list = []
    similarity_scores = []  #  유사도 저장용
    for i in range(panel_count):
        role_name, role_prompt = PANEL_ROLES[i]
        feedback = f"[{role_name}]\n"

        for chunk in chunks:
            docs_with_score = vector_db.similarity_search_with_score(chunk, k=3)
            context = "\n".join([doc.page_content for doc, _ in docs_with_score])
            
            # 유사도 계산
            scores = [score for _, score in docs_with_score]
            converted_similarities = [1 / (1 + score) for score in scores]  # 안정적인 0~1 정규화
            avg_score = sum(converted_similarities) / len(converted_similarities)
            similarity_scores.append(avg_score)

            prompt = f"""{role_prompt}

            [발표 내용]
            {chunk}

            [제안서 내용]
            {context}

            위 발표와 제안서를 비교해 평가하고 개선점을 피드백해줘."""
            
            llm = ChatOpenAI()
            feedback_chunk = llm.predict(prompt)
            feedback += f"- 발표 문단 평가: {feedback_chunk}\n"

        feedback_list.append(feedback)

    # 적합도 점수 (0~100)
    average_similarity = sum(similarity_scores) / len(similarity_scores) if similarity_scores else 0
    suitability_score = int(min(max(average_similarity * 100, 0), 100))
    
    return feedback_list, suitability_score
# 발표 평가 전체 흐름 함수

def evaluate_pitch_audio(file: UploadFile, user_panel_count: int, doc_title: str) -> PitchEvaluateResponse:
    transcript = transcribe_audio(file)
    vector_db = load_proposal_vector_db(doc_title)
    panel_feedback, suitability_score = run_evaluation(transcript, user_panel_count, vector_db)

    return PitchEvaluateResponse(
        transcript=transcript,
        panel_feedback=panel_feedback,
        suitability_score=suitability_score,
    )