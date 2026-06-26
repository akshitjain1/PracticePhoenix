import pytest
from sqlalchemy import select
from app.database.database import SessionLocal
from app.database.init_db import initialize_database
from app.models.history import DailyHistory
from app.scheduler.job_runner import JobRunner
from app.scheduler.scheduler_service import SchedulerService


@pytest.fixture(autouse=True)
def setup_db():
    initialize_database()


def test_scheduler_registration():
    service = SchedulerService()
    service.configure_jobs()
    
    job = service.scheduler.get_job("morning_brief_job")
    assert job is not None
    assert job.name == "morning_broadcast_job"
    assert str(job.trigger).startswith("cron[")


@pytest.mark.anyio
async def test_job_runner_execution_and_history_persistence():
    runner = JobRunner()
    
    content = await runner.run_morning_brief(bot_app=None, force=True)
    
    assert "Executive Communication" in content or "Vocabulary" in content
    
    with SessionLocal() as session:
        records = session.execute(select(DailyHistory)).scalars().all()
        assert len(records) > 0
        assert any(r.content == content for r in records)
