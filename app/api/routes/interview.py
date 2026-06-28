from pydantic import BaseModel
from typing import List
from fastapi import APIRouter, HTTPException
from app.services.interview_service import InterviewService


router = APIRouter(tags=["Interview"])


class InterviewQuestionResponse(BaseModel):
    session_id: int
    question_id: int
    topic: str
    question_text: str
    difficulty: str


class InterviewAnswerRequest(BaseModel):
    user_id: str = "default_user"
    answer_text: str


class InterviewAnswerResponse(BaseModel):
    evaluation_report_md: str
    overall_score: float
    technical_accuracy: float
    communication: float
    completeness: float
    missing_points: List[str]
    suggested_follow_up: str
    next_question_text: str


@router.get("/interview/question", response_model=InterviewQuestionResponse)
def get_interview_question(user_id: str = "default_user", category: str = "general"):
    """Orchestrates InterviewService to launch or continue an adaptive interview session and retrieve the current question."""
    service = InterviewService()
    sess = service.session_service.get_active_session(user_id)
    if not sess:
        sess = service.session_service.start_session(user_id, category)

    q_obj, topic = service.question_service.select_next_question(sess.id, category)
    return InterviewQuestionResponse(
        session_id=sess.id,
        question_id=q_obj.id,
        topic=topic,
        question_text=q_obj.question_text,
        difficulty=q_obj.difficulty
    )


@router.post("/interview/answer", response_model=InterviewAnswerResponse)
def post_interview_answer(request: InterviewAnswerRequest):
    """Orchestrates InterviewService to evaluate candidate answer and record attempt statistics."""
    service = InterviewService()
    sess = service.session_service.get_active_session(request.user_id)
    if not sess:
        raise HTTPException(status_code=400, detail="No active interview session found for this user.")

    report_md = service.process_answer(request.user_id, request.answer_text)
    if not report_md:
        raise HTTPException(status_code=400, detail="Failed to process interview answer.")

    attempts = service.repo.get_session_attempts(sess.id)
    if not attempts:
        raise HTTPException(status_code=500, detail="Evaluation succeeded but attempt was not recorded.")

    latest_attempt = attempts[-1]
    latest_q = service.repo.get_latest_question(sess.id)
    next_q_text = latest_q.question_text if latest_q else ""

    missing = []
    if latest_attempt.missing_points:
        import json
        try:
            missing = json.loads(latest_attempt.missing_points)
        except Exception:
            missing = [latest_attempt.missing_points]

    return InterviewAnswerResponse(
        evaluation_report_md=report_md,
        overall_score=latest_attempt.overall_score,
        technical_accuracy=latest_attempt.technical_accuracy,
        communication=latest_attempt.communication,
        completeness=latest_attempt.completeness,
        missing_points=missing,
        suggested_follow_up=latest_attempt.suggested_follow_up or "",
        next_question_text=next_q_text
    )
