import json
from datetime import datetime, timezone
from typing import List, Optional
from sqlalchemy import select, update
from app.database.database import SessionLocal
from app.models.interview import (
    InterviewSession,
    InterviewQuestion,
    InterviewAttempt,
)


class InterviewRepository:

    def get_active_session(self, user_id: str) -> Optional[InterviewSession]:
        with SessionLocal() as session:
            stmt = (
                select(InterviewSession)
                .where(
                    InterviewSession.user_id == user_id,
                    InterviewSession.status == "ACTIVE"
                )
                .order_by(InterviewSession.started_at.desc())
            )
            return session.execute(stmt).scalars().first()

    def create_session(self, user_id: str, category: str) -> InterviewSession:
        with SessionLocal() as session:
            session.execute(
                update(InterviewSession)
                .where(
                    InterviewSession.user_id == user_id,
                    InterviewSession.status == "ACTIVE"
                )
                .values(status="STOPPED")
            )

            new_sess = InterviewSession(
                user_id=user_id,
                category=category,
                status="ACTIVE",
                started_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc),
            )
            session.add(new_sess)
            session.commit()
            session.refresh(new_sess)
            return new_sess

    def update_session_status(self, session_id: int, status: str):
        with SessionLocal() as session:
            session.execute(
                update(InterviewSession)
                .where(InterviewSession.id == session_id)
                .values(status=status, updated_at=datetime.now(timezone.utc))
            )
            session.commit()

    def add_question(self, session_id: int, question_text: str, difficulty: str) -> InterviewQuestion:
        with SessionLocal() as session:
            q = InterviewQuestion(
                session_id=session_id,
                question_text=question_text,
                difficulty=difficulty,
                asked_at=datetime.now(timezone.utc)
            )
            session.add(q)
            session.commit()
            session.refresh(q)
            return q

    def get_latest_question(self, session_id: int) -> Optional[InterviewQuestion]:
        with SessionLocal() as session:
            stmt = (
                select(InterviewQuestion)
                .where(InterviewQuestion.session_id == session_id)
                .order_by(InterviewQuestion.asked_at.desc())
            )
            return session.execute(stmt).scalars().first()

    def add_attempt(
        self,
        question_id: int,
        user_answer: str,
        overall_score: float,
        technical_accuracy: float,
        communication: float,
        completeness: float,
        missing_points: List[str],
        suggested_follow_up: str,
    ) -> InterviewAttempt:
        with SessionLocal() as session:
            attempt = InterviewAttempt(
                question_id=question_id,
                user_answer=user_answer,
                overall_score=overall_score,
                technical_accuracy=technical_accuracy,
                communication=communication,
                completeness=completeness,
                missing_points=json.dumps(missing_points),
                suggested_follow_up=suggested_follow_up,
                evaluated_at=datetime.now(timezone.utc),
            )
            session.add(attempt)
            session.commit()
            session.refresh(attempt)
            return attempt

    def get_session_attempts(self, session_id: int) -> List[InterviewAttempt]:
        with SessionLocal() as session:
            stmt = (
                select(InterviewAttempt)
                .join(InterviewQuestion, InterviewAttempt.question_id == InterviewQuestion.id)
                .where(InterviewQuestion.session_id == session_id)
                .order_by(InterviewAttempt.evaluated_at.asc())
            )
            return list(session.execute(stmt).scalars().all())
