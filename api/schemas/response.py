from pydantic import BaseModel
from typing import List

class PitchEvaluateResponse(BaseModel): #발표 음성 관련 
    transcript: str
    panel_feedback: List[str]