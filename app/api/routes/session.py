from fastapi import APIRouter
from app.services.daily_service import DailyService
from app.ai.schemas.daily_schema import DailyBrief


router = APIRouter(tags=["Session"])


@router.get("/session/today", response_model=DailyBrief)
def get_today_session():
    """Orchestrates DailyService to generate today's complete study session brief."""
    service = DailyService()
    return service.generate_daily_brief()
