from pydantic import BaseModel
from typing import List, Optional

class ChunkRequest(BaseModel):
    file_path: str  # 로컬 경로 or 업로드된 S3 경로 등

class SubChunk(BaseModel):
    subtitle: str
    content: str
    tables: List[str] = []

class Chunk(BaseModel):
    section_title: str
    content: Optional[str] = ""  # 소제목 없이 바로 본문이 나올 경우 대비
    subsections: List[SubChunk] = []
    tables: List[str] = []  # 표만 있는 경우를 위한 처리

class FillMissingPartsRequest(BaseModel):
    incomplete_text: str  # 미완성 문서
    reference_texts: List[str]  # 참고 문서들

class ScriptEvaluateRequest(BaseModel):
    script_text: str

class SimilarityAnalyzeRequest(BaseModel):
    file_path: str
    top_k: int = 3
class InitialSetupRequest(BaseModel):
    company_name: str
    service_description: str
    judge_count: int

class SimilarityAnalyzeRequest(BaseModel):
    doc_title: str
    top_k: int

class FillMissingPartsRequest(BaseModel):
    incomplete_text: str
    reference_texts: List[str]