from datetime import date
import pytest
from app.database.init_db import initialize_database
from app.services.health_service import HealthService
from app.services.backup_service import BackupService
from app.services.startup_diagnostics_service import StartupDiagnosticsService
from app.scheduler.job_runner import JobRunner
from app.repositories.history_repository import HistoryRepository


@pytest.fixture(autouse=True)
def setup_db():
    initialize_database()


def test_health_service_subsystem():
    hs = HealthService()
    summary = hs.get_health_summary()
    assert "System Health Report" in summary
    assert "Database Connectivity" in summary
    
    stat = hs.check_health()
    assert stat.database in ["UP", "DOWN"]
    assert stat.status in ["HEALTHY", "DEGRADED", "UNHEALTHY"]


def test_backup_service_retention_policy(tmp_path):
    bk_dir = tmp_path / "test_backups"
    bk_dir.mkdir()
    
    for i in range(16):
        dummy = bk_dir / f"preparation_backup_20260101_0000{i:02d}.db"
        dummy.touch()
    
    srv = BackupService(backup_dir=str(bk_dir))
    new_bk = srv.create_backup()
    
    remaining = sorted(list(bk_dir.glob("preparation_backup_*.db")), key=lambda p: p.name)
    assert len(remaining) <= 14
    assert new_bk.exists()


@pytest.mark.anyio
async def test_scheduled_job_idempotency_prevention():
    repo = HistoryRepository()
    runner = JobRunner()
    
    today = date.today()
    if not repo.exists_for_date(today):
        repo.save_history("Test dummy brief for idempotency check.")
        
    res = await runner.run_morning_brief(force=False)
    assert res == "SKIPPED_DUPLICATE"


def test_startup_diagnostics_execution():
    assert StartupDiagnosticsService.run_diagnostics() is True
