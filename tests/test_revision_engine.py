from datetime import date, timedelta
import pytest
from app.database.init_db import initialize_database
from app.services.learning_engine import LearningEngine
from app.services.revision_service import RevisionService


@pytest.fixture(autouse=True)
def setup_db():
    initialize_database()


def test_revision_scheduling_and_duplicate_prevention():
    rev_service = RevisionService()
    today = date(2026, 6, 26)
    
    # Schedule new revisions
    rev_service.schedule_new_revisions("operating_systems", "Mutex", [1, 3, 7], today)
    
    due_day1 = rev_service.get_due_topics("operating_systems", today + timedelta(days=1))
    assert any(item.topic == "Mutex" for item in due_day1)
    
    # Test duplicate prevention (calling schedule again)
    rev_service.schedule_new_revisions("operating_systems", "Mutex", [1, 3, 7], today)
    due_day1_again = rev_service.get_due_topics("operating_systems", today + timedelta(days=1))
    assert len([item for item in due_day1_again if item.topic == "Mutex" and item.stage == 0]) == 1


def test_learning_engine_plan_merging_and_completion():
    engine = LearningEngine()
    test_date = date(2026, 6, 26)
    
    # Complete day 1 to schedule revisions for day 2
    engine.complete_today(test_date)
    
    # On day 2 (test_date + 1 day), topics scheduled with offset 1 should be due
    next_day = test_date + timedelta(days=1)
    plan = engine.get_today_plan(next_day)
    
    assert "operating_systems" in plan.topics
    # Verify due revision is retrieved and merged
    assert any(len(topics) > 0 for topics in plan.due_revisions.values())
    
    # Complete day 2 to verify archive/advancement
    engine.complete_today(next_day)
    plan_after = engine.get_today_plan(next_day)
    # The due revisions for that exact day should now be advanced/cleared
    assert plan_after.due_revisions.get("operating_systems", []) == []
