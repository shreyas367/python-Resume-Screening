from fastapi import APIRouter
from pydantic import BaseModel
from app.services.matcher import match_resume

router = APIRouter()

class InputData(BaseModel):
    resume: str
    job: str

@router.post("/match")
def match(data: InputData):
    return match_resume(data.resume, data.job)