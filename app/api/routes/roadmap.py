from pydantic import BaseModel
from typing import List
from fastapi import APIRouter
from app.services.progress_service import ProgressService


router = APIRouter(tags=["Roadmap"])


class RoadmapCategoryItem(BaseModel):
    category: str
    remaining_lessons: int


class RoadmapResponse(BaseModel):
    total_remaining_lessons: int
    estimated_days_to_complete: int
    categories: List[RoadmapCategoryItem]


@router.get("/roadmap", response_model=RoadmapResponse)
def get_roadmap():
    """Orchestrates ProgressService to project remaining curriculum milestones and estimated study days."""
    service = ProgressService()
    data = service.calculate_completion_metrics()
    remaining_total = data["overall_total"] - data["overall_completed"]
    est_days = remaining_total

    cats = []
    for cat, info in data["categories"].items():
        if info["remaining"] > 0:
            cats.append(RoadmapCategoryItem(category=cat, remaining_lessons=info["remaining"]))

    return RoadmapResponse(
        total_remaining_lessons=remaining_total,
        estimated_days_to_complete=est_days,
        categories=cats
    )
