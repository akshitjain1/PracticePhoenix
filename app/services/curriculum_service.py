from typing import Dict
from app.curriculum.schemas import LearningPlan
from app.repositories.curriculum_repository import CurriculumRepository
from app.repositories.progress_repository import ProgressRepository


class CurriculumService:

    CATEGORIES = [
        "communication",
        "operating_systems",
        "dbms",
        "computer_networks",
        "linux",
        "backend",
        "ai_engineering",
        "dsa",
        "interview_preparation"
    ]

    def __init__(self):
        self.repo = ProgressRepository()
        self.curriculum_repo = CurriculumRepository()

    def get_today_plan(self) -> LearningPlan:
        topics_map = {}
        day = 1
        for cat in self.CATEGORIES:
            idx = self.repo.get_index(cat)
            asset = self.curriculum_repo.get_topic_by_index(cat, idx)
            topics_map[cat] = asset
            day = max(day, idx + 1)

        # Alias mappings for DailyBrief compatibility
        topics_map["executive_communication"] = topics_map["communication"]
        topics_map["engineering_insight"] = topics_map["linux"]

        return LearningPlan(day=day, topics=topics_map)

    def get_today_topics(self) -> Dict[str, str]:
        plan = self.get_today_plan()
        return {cat: asset.topic for cat, asset in plan.topics.items()}

    def complete_today(self):
        for cat in self.CATEGORIES:
            self.repo.increment(cat)