from pydantic import BaseModel
from typing import List

class PitchEvaluateResponse(BaseModel): #발표 음성 관련 
    transcript: str
    panel_feedback: List[str]

class FillMissingPartsResponse(BaseModel):
    completed_text: str  # 보완된 최종 문서

class ScriptEvaluateResponse(BaseModel):
    correct_sentences: List[str]
    incorrect_sentences: List[str]

class ScoredSentence(BaseModel):
    sentence_index: int
    sentence: str
    score: float

class SimilarityAnalyzeResponse(BaseModel):
    average_similarity: float
    most_similar_sentences: List[ScoredSentence]
    least_similar_sentences: List[ScoredSentence]
    evaluated_sentences : List[str]
    suitability_score: int 

class SummaryResponse(BaseModel):
    summary: str

class JudgeResponse(BaseModel):
    judges: List[str]

class FitScoreResponse(BaseModel):
    score_by_category: dict

class TrendSuggestionResponse(BaseModel):
    suggestions: List[str]