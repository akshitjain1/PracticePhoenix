from typing import Optional
from app.models.interview import InterviewSession
from app.repositories.interview_repository import InterviewRepository


class SessionService:

    def __init__(self):
        self.repo = InterviewRepository()

    def get_active_session(self, user_id: str) -> Optional[InterviewSession]:
        return self.repo.get_active_session(user_id)

    def start_session(self, user_id: str, category: str) -> InterviewSession:
        return self.repo.create_session(user_id, category)

    def stop_session(self, user_id: str) -> bool:
        sess = self.get_active_session(user_id)
        if sess:
            self.repo.update_session_status(sess.id, "STOPPED")
            return True
        return False
