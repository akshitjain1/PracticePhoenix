from typing import Optional
from app.services.session_service import SessionService
from app.services.question_service import QuestionService
from app.services.evaluation_service import EvaluationService
from app.repositories.interview_repository import InterviewRepository


class InterviewService:

    def __init__(self):
        self.session_service = SessionService()
        self.question_service = QuestionService()
        self.eval_service = EvaluationService()
        self.repo = InterviewRepository()

    def start_interview(self, user_id: str, category: str = "general") -> str:
        sess = self.session_service.start_session(user_id, category)
        q_obj, topic = self.question_service.select_next_question(sess.id, category)
        return (
            "🔥 *Adaptive AI Interview Session Started*\n"
            f"🎯 *Focus Domain*: {topic}\n\n"
            f"❓ *Question 1*:\n{q_obj.question_text}\n\n"
            "_Type your detailed technical answer directly in this chat._"
        )

    def stop_interview(self, user_id: str) -> str:
        sess = self.session_service.get_active_session(user_id)
        if not sess:
            return "⚠️ No active interview session found to stop."

        attempts = self.repo.get_session_attempts(sess.id)
        self.session_service.stop_session(user_id)

        if not attempts:
            return "🛑 Interview session stopped before any questions were answered."

        avg_score = round(sum(a.overall_score for a in attempts) / len(attempts), 1)
        return (
            "🛑 *Interview Session Concluded*\n\n"
            f"📊 *Questions Completed*: {len(attempts)}\n"
            f"🏆 *Average Evaluation Score*: {avg_score}/10.0\n\n"
            "Great practice! Use `/grill-me` anytime to launch another session."
        )

    def process_answer(self, user_id: str, answer_text: str) -> Optional[str]:
        sess = self.session_service.get_active_session(user_id)
        if not sess:
            return None

        latest_q = self.repo.get_latest_question(sess.id)
        if not latest_q:
            return "⚠️ Session error: No active question found."

        eval_res = self.eval_service.evaluate_response(latest_q.question_text, answer_text)

        self.repo.add_attempt(
            question_id=latest_q.id,
            user_answer=answer_text,
            overall_score=eval_res.overall_score,
            technical_accuracy=eval_res.technical_accuracy,
            communication=eval_res.communication,
            completeness=eval_res.completeness,
            missing_points=eval_res.missing_points,
            suggested_follow_up=eval_res.suggested_follow_up,
        )

        missing_str = "\n".join(f"• {m}" for m in eval_res.missing_points) if eval_res.missing_points else "• None!"

        next_q, topic = self.question_service.select_next_question(sess.id, sess.category)
        attempt_num = len(self.repo.get_session_attempts(sess.id)) + 1

        response_md = (
            "📊 *Attempt Evaluation Report*\n"
            f"⭐ *Overall Score*: {eval_res.overall_score}/10.0\n"
            f"  • Tech Accuracy: {eval_res.technical_accuracy}/10.0\n"
            f"  • Communication: {eval_res.communication}/10.0\n"
            f"  • Completeness: {eval_res.completeness}/10.0\n\n"
            f"🔍 *Missing Points*:\n{missing_str}\n\n"
            f"💡 *Interviewer Tip*: {eval_res.suggested_follow_up}\n"
            "----------------------------------------\n"
            f"❓ *Question {attempt_num}*:\n{next_q.question_text}"
        )

        return response_md

    def get_current_score(self, user_id: str) -> str:
        sess = self.session_service.get_active_session(user_id)
        if not sess:
            return "⚠️ You are not currently in an active interview session."

        attempts = self.repo.get_session_attempts(sess.id)
        if not attempts:
            return "ℹ️ Active session started, but no questions evaluated yet."

        avg_score = round(sum(a.overall_score for a in attempts) / len(attempts), 1)
        return (
            "📈 *Live Interview Performance*\n"
            f"• Questions Evaluated: {len(attempts)}\n"
            f"• Current Average Score: {avg_score}/10.0"
        )

    def get_hint(self, user_id: str) -> str:
        sess = self.session_service.get_active_session(user_id)
        if not sess:
            return "⚠️ No active interview session."
        latest_q = self.repo.get_latest_question(sess.id)
        if not latest_q:
            return "⚠️ No active question."

        return f"💡 *Hint*: Think carefully about memory hierarchy, network latency, and failure isolation for:\n_{latest_q.question_text}_"

    def skip_question(self, user_id: str) -> str:
        sess = self.session_service.get_active_session(user_id)
        if not sess:
            return "⚠️ No active interview session."

        next_q, topic = self.question_service.select_next_question(sess.id, sess.category)
        return f"⏭️ *Question Skipped*\n\n❓ *Next Question*:\n{next_q.question_text}"
