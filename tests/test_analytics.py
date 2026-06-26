import pytest
from app.database.init_db import initialize_database
from app.repositories.history_repository import HistoryRepository
from app.repositories.progress_repository import ProgressRepository
from app.services.progress_service import ProgressService
from app.services.statistics_service import StatisticsService
from app.services.analytics_service import AnalyticsService


@pytest.fixture(autouse=True)
def setup_db():
    initialize_database()


def test_analytics_and_progress_subsystem():
    # Setup dummy history and progress
    hist_repo = HistoryRepository()
    hist_repo.save_history("Brief day 1")
    hist_repo.save_history("Brief day 2")
    
    prog_repo = ProgressRepository()
    prog_repo.get_index("operating_systems")
    prog_repo.increment("operating_systems")
    
    ps = ProgressService()
    ss = StatisticsService()
    as_srv = AnalyticsService()
    
    # 1. Test progress metrics
    prog_summary = ps.get_progress_summary()
    assert "Curriculum Completion Overview" in prog_summary
    assert "Operating Systems" in prog_summary
    
    # 2. Test roadmap estimation
    roadmap = ps.get_roadmap_summary()
    assert "Remaining Curriculum Roadmap" in roadmap
    assert "Estimated Days to Complete" in roadmap
    
    # 3. Test stats & streak
    stats = ss.get_stats_summary()
    assert "Platform Analytics" in stats
    assert "Total Briefs Generated" in stats
    
    streak = ss.get_streak_summary()
    assert "Daily Study Streak Report" in streak
    
    # 4. Test weaknesses ranking
    weaknesses = as_srv.get_weaknesses_summary()
    assert "Domain Weaknesses" in weaknesses
    assert "1." in weaknesses
