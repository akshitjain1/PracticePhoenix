import pytest
from app.database.init_db import initialize_database
from app.services.coaching_service import CoachingService
from app.services.daily_service import DailyService
from app.ai.formatter import TelegramFormatter


@pytest.fixture(autouse=True)
def setup_db():
    initialize_database()


def test_coaching_subsystem():
    coaching = CoachingService()
    
    # 1. Test input metric gathering
    metrics = coaching.gather_coaching_metrics()
    assert "overall_completion_pct" in metrics
    assert "current_streak" in metrics
    assert "weakest_category" in metrics
    
    # 2. Test advice generation
    advice = coaching.generate_coaching_advice()
    assert "Executive Career Mentor" in advice or "streak" in advice
    
    # 3. Test formatter integration
    service = DailyService()
    brief = service.generate_daily_brief()
    assert brief.personal_coaching != ""
    
    formatter = TelegramFormatter()
    formatted = formatter.format(brief)
    assert "## 🎯 Personal Coaching" in formatted
    assert brief.personal_coaching in formatted
