import pytest
from app.database.init_db import initialize_database
from app.services.activity_service import ActivityService
from app.services.coaching_service import CoachingService
from app.services.analytics_service import AnalyticsService


@pytest.fixture(autouse=True)
def setup_db():
    initialize_database()


def test_activity_tracking_subsystem():
    service = ActivityService()
    
    # 1. Test event recording & persistence
    service.log_interaction("search_executed", "kubernetes")
    service.log_interaction("search_executed", "system design")
    service.log_interaction("topic_reopened", "dbms")
    
    # 2. Test event aggregation
    summary = service.get_activity_summary()
    assert summary["total_interactions"] >= 3
    assert summary["by_type"]["search_executed"] >= 2
    assert summary["by_type"]["topic_reopened"] >= 1
    
    # 3. Test exposure to coaching & analytics
    cs = CoachingService()
    c_metrics = cs.gather_coaching_metrics()
    assert "activity_volume" in c_metrics
    assert c_metrics["activity_volume"] >= 3
    
    as_srv = AnalyticsService()
    weak_str = as_srv.get_weaknesses_summary()
    assert "learning interactions" in weak_str
