from pydantic import BaseModel, Field
from typing import List, Dict


class TopicAsset(BaseModel):
    id: str
    topic: str
    difficulty: str  # "easy", "medium", "hard"
    estimated_minutes: int
    tags: List[str]
    prerequisites: List[str]
    revision_schedule: List[int]


class LearningPlan(BaseModel):
    day: int
    topics: Dict[str, TopicAsset]
    due_revisions: Dict[str, List[str]] = Field(default_factory=dict)
