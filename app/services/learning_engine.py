from datetime import date
from typing import Dict, List
from app.curriculum.schemas import LearningPlan
from app.services.curriculum_service import CurriculumService
from app.services.revision_service import RevisionService
from app.services.activity_service import ActivityService
from app.utils.logger import app_logger


class LearningEngine:

    def __init__(self):
        self.curriculum = CurriculumService()
        self.revision = RevisionService()
        self._current_due_ids: List[int] = []

    def get_today_plan(self, target_date: date = None) -> LearningPlan:
        ref_date = target_date or date.today()
        base_plan = self.curriculum.get_today_plan()
        due_revisions_map: Dict[str, List[str]] = {}
        self._current_due_ids = []

        for cat in self.curriculum.CATEGORIES:
            asset = base_plan.topics[cat]
            due_items = self.revision.get_due_topics(cat, ref_date)
            if due_items:
                rev_topics = [item.topic for item in due_items]
                due_revisions_map[cat] = rev_topics
                self._current_due_ids.extend([item.id for item in due_items])
                rev_str = ", ".join(rev_topics)
                asset.topic = f"{asset.topic} (Due Revision Focus: {rev_str})"

        base_plan.due_revisions = due_revisions_map
        return base_plan

    def complete_today(self, target_date: date = None):
        ref_date = target_date or date.today()
        plan = self.curriculum.get_today_plan()
        self.curriculum.complete_today()
        ActivityService().log_interaction("lesson_completed", f"{len(self.curriculum.CATEGORIES)}_tracks")

        for cat in self.curriculum.CATEGORIES:
            asset = plan.topics[cat]
            clean_topic = asset.topic.split(" (Due Revision Focus:")[0]
            self.revision.schedule_new_revisions(
                cat, clean_topic, asset.revision_schedule, ref_date
            )

        if self._current_due_ids:
            num_revs = len(self._current_due_ids)
            self.revision.advance_completed_revisions(self._current_due_ids)
            ActivityService().log_interaction("revision_completed", f"{num_revs}_topics")
            self._current_due_ids = []

        app_logger.info("LearningEngine daily lifecycle completed.")
