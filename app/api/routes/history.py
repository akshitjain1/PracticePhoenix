from pydantic import BaseModel
from typing import List
from fastapi import APIRouter
from app.services.history_service import HistoryService


router = APIRouter(tags=["History"])


class BriefHistoryItem(BaseModel):
    id: int
    generated_at: str
    content: str


class HistoryResponse(BaseModel):
    total_returned: int
    briefs: List[BriefHistoryItem]


@router.get("/history", response_model=HistoryResponse)
def get_history(limit: int = 50):
    """Orchestrates HistoryService repository to retrieve archived daily briefs."""
    service = HistoryService()
    records = service.repo.get_recent_briefs(limit)
    items = [
        BriefHistoryItem(
            id=r.id,
            generated_at=r.generated_at.isoformat(),
            content=r.content
        )
        for r in records
    ]
    return HistoryResponse(total_returned=len(items), briefs=items)
