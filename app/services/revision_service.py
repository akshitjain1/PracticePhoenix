from datetime import date, timedelta
from typing import List
from app.models.revision import RevisionQueue
from app.repositories.revision_repository import RevisionRepository
from app.utils.logger import app_logger


class RevisionService:

    def __init__(self):
        self.repo = RevisionRepository()

    def schedule_new_revisions(
        self,
        category: str,
        topic: str,
        revision_schedule: List[int],
        start_date: date = None,
    ):
        base_date = start_date or date.today()
        for stage, days_offset in enumerate(revision_schedule):
            rev_date = base_date + timedelta(days=days_offset)
            self.repo.schedule_if_not_exists(category, topic, rev_date, stage)
        app_logger.debug(
            f"Scheduled {len(revision_schedule)} revision stages for {category}: {topic}"
        )

    def get_due_topics(
        self, category: str, target_date: date = None
    ) -> List[RevisionQueue]:
        ref_date = target_date or date.today()
        return self.repo.get_due_today(category, ref_date)

    def advance_completed_revisions(self, completed_ids: List[int]):
        self.repo.remove_by_ids(completed_ids)
        app_logger.debug(f"Advanced/Archived {len(completed_ids)} completed revisions.")
