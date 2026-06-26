import pytest
from unittest.mock import MagicMock
from app.database.init_db import initialize_database
from app.ai.schemas.daily_schema import CSSection, DailyBrief
from app.services.daily_service import DailyService
from app.services.generators.cs_generator import CSSectionGenerator


@pytest.fixture(autouse=True)
def setup_db():
    initialize_database()


def test_generator_prompt_loading_and_fallback(monkeypatch):
    gen = CSSectionGenerator("operating_systems.md")
    
    # Verify prompt loading
    prompt = gen._load_prompt(topic="Deadlocks")
    assert "Deadlocks" in prompt
    assert "Operating Systems" in prompt
    
    # Simulate network failure causing fallback
    mock_ai = MagicMock()
    mock_ai.generate.side_effect = Exception("API Timeout")
    monkeypatch.setattr(gen, "ai", mock_ai)
    
    fallback = CSSection(
        topic="Deadlocks",
        interview_question="Fallback Q",
        why_interviewer_asks="Fallback Why",
        ideal_answer="Fallback Ans",
        engineering_explanation="Fallback Eng",
        real_world_example="Fallback Ex",
        follow_up_questions=[]
    )
    
    res = gen.generate(fallback, topic="Deadlocks")
    assert res.topic == "Deadlocks"
    assert res.ideal_answer == "Fallback Ans"
    assert mock_ai.generate.call_count == 3


def test_daily_service_orchestration(monkeypatch):
    # Mock AIGenerator to raise exception so all generators return fallback cleanly
    from app.services.generators import base_generator
    mock_ai = MagicMock()
    mock_ai.generate.side_effect = Exception("Simulated Offline")
    monkeypatch.setattr(base_generator.AIGenerator, "generate", mock_ai.generate)
    
    service = DailyService()
    brief = service.generate_daily_brief()
    
    assert isinstance(brief, DailyBrief)
    assert brief.operating_systems.topic is not None
    assert brief.dsa.problem is not None
