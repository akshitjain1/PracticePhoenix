from typing import Tuple
from app.repositories.curriculum_repository import CurriculumRepository
from app.repositories.interview_repository import InterviewRepository
from app.services.analytics_service import AnalyticsService
from app.models.interview import InterviewQuestion


class QuestionService:

    def __init__(self):
        self.curriculum_repo = CurriculumRepository()
        self.interview_repo = InterviewRepository()
        self.analytics_service = AnalyticsService()

    def select_next_question(self, session_id: int, category: str) -> Tuple[InterviewQuestion, str]:
        attempts = self.interview_repo.get_session_attempts(session_id)
        if not attempts:
            difficulty = "Medium"
        else:
            last_score = attempts[-1].overall_score
            if last_score >= 8.0:
                difficulty = "Hard"
            elif last_score < 5.0:
                difficulty = "Easy"
            else:
                difficulty = "Medium"

        target_cat = category
        if not target_cat or target_cat == "general":
            weaknesses = self.analytics_service.rank_weaknesses()
            target_cat = weaknesses[0]["category"] if weaknesses else "operating_systems"

        try:
            assets = self.curriculum_repo.load_category(target_cat)
            idx = len(attempts) % len(assets) if assets else 0
            topic_asset = assets[idx] if assets else None
            topic_title = topic_asset.topic if topic_asset else "System Architecture"
        except Exception:
            topic_title = "Distributed Systems & Concurrency"

        q_text = (
            f"[{difficulty}] In the context of {target_cat.replace('_', ' ').title()}, "
            f"explain the core design tradeoffs and failure modes of '{topic_title}'."
        )

        q_obj = self.interview_repo.add_question(session_id, q_text, difficulty)
        return q_obj, topic_title
