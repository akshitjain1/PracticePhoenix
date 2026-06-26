from typing import Dict
from app.repositories.activity_repository import ActivityRepository
from app.utils.logger import app_logger


class ActivityService:

    def __init__(self):
        self.repo = ActivityRepository()

    def log_interaction(self, event_type: str, details: str = ""):
        try:
            self.repo.record_event(event_type, details)
            app_logger.debug(f"Telemetry recorded: {event_type} ({details})")
        except Exception as e:
            app_logger.warning(f"Non-blocking telemetry capture failed for {event_type}: {e}")

    def get_activity_summary(self) -> Dict:
        try:
            counts = self.repo.get_event_counts()
            total = sum(counts.values())
            return {"total_interactions": total, "by_type": counts}
        except Exception as e:
            app_logger.warning(f"Failed to retrieve activity summary: {e}")
            return {"total_interactions": 0, "by_type": {}}
