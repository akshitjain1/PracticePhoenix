from pydantic import BaseModel
from typing import List
from fastapi import APIRouter
from app.services.revision_service import RevisionService


router = APIRouter(tags=["Revision"])


class CategoryRevision(BaseModel):
    category: str
    pending_count: int
    due_topics: List[str]


class RevisionResponse(BaseModel):
    total_pending: int
    categories: List[CategoryRevision]


@router.get("/revision", response_model=RevisionResponse)
def get_revisions():
    """Orchestrates RevisionService to return pending revision counts and due topics across categories."""
    service = RevisionService()
    counts = service.repo.get_pending_counts()
    
    # Standard categories to check if not present in counts
    all_cats = [
        "operating_systems", "dbms", "computer_networks", "linux", 
        "backend", "ai_engineering", "dsa", "system_design", "communication"
    ]
    for c in all_cats:
        if c not in counts:
            counts[c] = 0

    cats = []
    total = 0
    for cat, count in sorted(counts.items()):
        due = [r.topic for r in service.get_due_topics(cat)]
        cats.append(CategoryRevision(category=cat, pending_count=count, due_topics=due))
        total += count

    return RevisionResponse(total_pending=total, categories=cats)
