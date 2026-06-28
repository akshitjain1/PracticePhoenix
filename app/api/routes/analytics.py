from pydantic import BaseModel
from typing import List
from fastapi import APIRouter
from app.services.analytics_service import AnalyticsService


router = APIRouter(tags=["Analytics"])


class WeaknessRankingItem(BaseModel):
    category: str
    pending_revisions: int
    remaining_lessons: int
    completion_pct: float
    weakness_score: int


class AnalyticsResponse(BaseModel):
    total_interactions: int
    weakness_rankings: List[WeaknessRankingItem]


@router.get("/analytics", response_model=AnalyticsResponse)
def get_analytics():
    """Orchestrates AnalyticsService to rank domain weaknesses derived from study telemetry."""
    service = AnalyticsService()
    rankings = service.rank_weaknesses()
    activity = service.activity_service.get_activity_summary()
    
    items = [WeaknessRankingItem.model_validate(r) for r in rankings]
    return AnalyticsResponse(
        total_interactions=activity.get("total_interactions", 0),
        weakness_rankings=items
    )
