import pytest
from app.database.init_db import initialize_database
from app.services.interview_service import InterviewService


@pytest.fixture(autouse=True)
def setup_db():
    initialize_database()


def test_adaptive_interview_subsystem():
    srv = InterviewService()
    uid = "test_user_404"
    
    # 1. Test session lifecycle & start
    start_msg = srv.start_interview(uid, "operating_systems")
    assert "Adaptive AI Interview Session Started" in start_msg
    assert "Question 1" in start_msg
    
    # 2. Test hint & live score before answer
    score_msg = srv.get_current_score(uid)
    assert "no questions evaluated yet" in score_msg
    
    hint_msg = srv.get_hint(uid)
    assert "Hint" in hint_msg
    
    # 3. Test candidate evaluation & attempt recording
    eval_msg = srv.process_answer(uid, "Virtual memory maps virtual addresses to physical pages via page tables.")
    assert eval_msg is not None
    assert "Attempt Evaluation Report" in eval_msg
    assert "Overall Score" in eval_msg
    assert "Question 2" in eval_msg
    
    # 4. Test live score after answer
    live_score = srv.get_current_score(uid)
    assert "Questions Evaluated: 1" in live_score
    
    # 5. Test question skip
    skip_msg = srv.skip_question(uid)
    assert "Question Skipped" in skip_msg
    
    # 6. Test session stop
    stop_msg = srv.stop_interview(uid)
    assert "Interview Session Concluded" in stop_msg
    assert "Average Evaluation Score" in stop_msg
