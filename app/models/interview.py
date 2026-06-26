from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Float
from app.database.models import Base


class InterviewSession(Base):

    __tablename__ = "interview_session"

    id = Column(Integer, primary_key=True)
    user_id = Column(String(100), index=True)
    category = Column(String(50))
    status = Column(String(20), default="ACTIVE")
    started_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))


class InterviewQuestion(Base):

    __tablename__ = "interview_question"

    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey("interview_session.id"), index=True)
    question_text = Column(Text)
    difficulty = Column(String(20), default="Medium")
    asked_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))


class InterviewAttempt(Base):

    __tablename__ = "interview_attempt"

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey("interview_question.id"), index=True)
    user_answer = Column(Text)
    overall_score = Column(Float, default=0.0)
    technical_accuracy = Column(Float, default=0.0)
    communication = Column(Float, default=0.0)
    completeness = Column(Float, default=0.0)
    missing_points = Column(Text, default="[]")
    suggested_follow_up = Column(Text, default="")
    evaluated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
