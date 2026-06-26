import pytest
from app.curriculum.schemas import LearningPlan, TopicAsset
from app.database.init_db import initialize_database
from app.repositories.curriculum_repository import CurriculumRepository
from app.services.curriculum_service import CurriculumService


@pytest.fixture(autouse=True)
def setup_db():
    initialize_database()


def test_curriculum_loading_and_validation():
    repo = CurriculumRepository()
    
    # Test loading each required asset category
    categories = [
        "communication",
        "operating_systems",
        "dbms",
        "computer_networks",
        "linux",
        "backend",
        "ai_engineering",
        "dsa",
        "interview_preparation"
    ]
    for cat in categories:
        assets = repo.load_category(cat)
        assert len(assets) > 0
        assert isinstance(assets[0], TopicAsset)
        assert assets[0].difficulty in ["easy", "medium", "hard"]
        assert isinstance(assets[0].revision_schedule, list)


def test_learning_plan_generation_and_advancement():
    service = CurriculumService()
    
    # Generate initial learning plan
    plan1 = service.get_today_plan()
    assert isinstance(plan1, LearningPlan)
    assert "operating_systems" in plan1.topics
    assert "executive_communication" in plan1.topics
    
    topic_os_day1 = plan1.topics["operating_systems"].topic
    
    # Advance progress
    service.complete_today()
    
    # Generate next plan
    plan2 = service.get_today_plan()
    topic_os_day2 = plan2.topics["operating_systems"].topic
    
    assert topic_os_day1 != topic_os_day2
