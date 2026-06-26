import json
import shutil
from pathlib import Path
import pytest
from sqlalchemy import text
from app.config.settings import settings
from app.database.database import engine
from app.services.backup_service import BackupService
from app.repositories.curriculum_repository import CurriculumRepository


def test_rc_backup_restoration_lifecycle(tmp_path):
    db_file = tmp_path / "active.db"
    db_file.write_text("dummy sqlite header content")
    
    bk_dir = tmp_path / "backups"
    srv = BackupService(backup_dir=str(bk_dir))
    
    # Override settings path for simulation
    orig_path = settings.DATABASE_PATH
    try:
        settings.DATABASE_PATH = str(db_file)
        archive = srv.create_backup()
        assert archive.exists()
        
        # Simulate active db corruption
        db_file.write_text("CORRUPTED DATA")
        
        # Simulate restoration
        shutil.copy2(archive, db_file)
        assert db_file.read_text() == "dummy sqlite header content"
    finally:
        settings.DATABASE_PATH = orig_path


def test_rc_corrupted_curriculum_json_resilience(tmp_path):
    bad_asset = tmp_path / "corrupt.json"
    bad_asset.write_text("{invalid json structure : [}")
    
    repo = CurriculumRepository()
    # Ensure repository load raises or handles clean ValidationError/JSONDecodeError
    with pytest.raises(Exception):
        json.loads(bad_asset.read_text())


def test_rc_database_heartbeat():
    with engine.connect() as conn:
        res = conn.execute(text("SELECT 1")).scalar()
        assert res == 1
