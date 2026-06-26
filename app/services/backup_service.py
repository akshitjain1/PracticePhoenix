import shutil
from pathlib import Path
from datetime import datetime
from app.config.settings import settings
from app.utils.logger import app_logger


class BackupService:

    def __init__(self, backup_dir: str = "backups"):
        self.backup_dir = Path(backup_dir)
        self.backup_dir.mkdir(parents=True, exist_ok=True)

    def create_backup(self) -> Path:
        db_path = Path(settings.DATABASE_PATH)
        if not db_path.exists():
            db_path.parent.mkdir(parents=True, exist_ok=True)
            db_path.touch()

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        dest_path = self.backup_dir / f"preparation_backup_{timestamp}.db"

        shutil.copy2(db_path, dest_path)
        app_logger.info(f"Database backup created successfully at {dest_path}")
        self._cleanup_old_backups()
        return dest_path

    def _cleanup_old_backups(self, retention: int = 14):
        backups = sorted(
            self.backup_dir.glob("preparation_backup_*.db"),
            key=lambda p: p.name
        )
        if len(backups) > retention:
            for old_bk in backups[:-retention]:
                try:
                    old_bk.unlink()
                    app_logger.debug(f"Removed expired backup archive: {old_bk}")
                except Exception as e:
                    app_logger.warning(f"Failed to remove old backup {old_bk}: {e}")
