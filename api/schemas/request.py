from pydantic import BaseModel
from typing import List

class FillMissingPartsRequest(BaseModel):
    incomplete_text: str  # 미완성 문서
    reference_texts: List[str]  # 참고 문서들

class ScriptEvaluateRequest(BaseModel):
    script_text: str

class SimilarityAnalyzeRequest(BaseModel):
    file_path: str
    top_k: int = 3
