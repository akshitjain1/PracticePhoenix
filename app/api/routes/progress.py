from pydantic import BaseModel
from typing import Dict
from fastapi import APIRouter
from app.services.progress_service import ProgressService


router = APIRouter(tags=["Progress"])


class CategoryProgressInfo(BaseModel):
    total: int
    completed: int
    current_index: int
    percentage: float
    remaining: int


class ProgressResponse(BaseModel):
    categories: Dict[str, CategoryProgressInfo]
    overall_completed: int
    overall_total: int
    overall_percentage: float


@router.get("/progress", response_model=ProgressResponse)
def get_progress():
    """Orchestrates ProgressService to return completion percentages and lesson counts."""
    service = ProgressService()
    data = service.calculate_completion_metrics()
    return ProgressResponse.model_validate(data)
