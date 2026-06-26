import pytest
from app.database.init_db import initialize_database
from app.repositories.history_repository import HistoryRepository
from app.services.history_service import HistoryService
from app.services.search_service import SearchService


@pytest.fixture(autouse=True)
def setup_db():
    initialize_database()


def test_knowledge_management_retrieval_and_search():
    repo = HistoryRepository()

    repo.save_history("Topic: Mutex locks in OS concurrency. Distributed systems design.")
    repo.save_history("Topic: Processes lifecycle and thread scheduling in Linux kernel.")

    hist_service = HistoryService()
    search_service = SearchService()

    # 1. Test history retrieval
    recent_text = hist_service.get_recent_briefs_text(limit=2)
    assert "Recent" in recent_text
    assert "Mutex" in recent_text or "Processes" in recent_text

    # 2. Test keyword search
    search_text = search_service.search_keyword("concurrency")
    assert "Mutex locks" in search_text
    assert "found" in search_text

    # 3. Test topic lookup
    topic_text = search_service.find_topic("Processes")
    assert "Latest Lesson" in topic_text
    assert "thread scheduling" in topic_text

    # 4. Test export generation
    md_export = hist_service.export_history("md")
    assert "# Daily AI Preparation Platform - Complete Study History" in md_export
    assert "Total Briefs Recorded" in md_export

    # Verify unsupported format error
    with pytest.raises(NotImplementedError):
        hist_service.export_history("pdf")
