import os
from pathlib import Path
from sqlalchemy import text
from app.config.settings import settings
from app.database.database import engine
from app.repositories.curriculum_repository import CurriculumRepository
from app.utils.logger import app_logger


class StartupDiagnosticsService:

    @staticmethod
    def run_diagnostics() -> bool:
        app_logger.info("Executing Production Startup Diagnostics...")
        errors = []

        if not settings.TELEGRAM_BOT_TOKEN or settings.TELEGRAM_BOT_TOKEN == "mock_token":
            if "PYTEST_CURRENT_TEST" not in os.environ:
                errors.append("Missing required TELEGRAM_BOT_TOKEN configuration.")

        if not settings.GROQ_API_KEY or settings.GROQ_API_KEY == "mock_key":
            if "PYTEST_CURRENT_TEST" not in os.environ:
                errors.append("Missing required GROQ_API_KEY configuration.")

        try:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            app_logger.info("✓ Database connectivity verified.")
        except Exception as e:
            errors.append(f"Database connectivity check failed: {e}")

        try:
            repo = CurriculumRepository()
            assets = repo.load_category("operating_systems")
            if not assets:
                errors.append("Curriculum asset directory loaded 0 lessons.")
            else:
                app_logger.info("✓ Curriculum JSON assets verified.")
        except Exception as e:
            errors.append(f"Curriculum assets check failed: {e}")

        try:
            export_dir = Path("data/exports")
            export_dir.mkdir(parents=True, exist_ok=True)
            test_file = export_dir / ".write_test"
            test_file.touch()
            test_file.unlink()
            app_logger.info("✓ Writable export directory verified.")
        except Exception as e:
            errors.append(f"Export directory write permission failed: {e}")

        if errors:
            err_report = "\n".join(f"  ❌ {err}" for err in errors)
            app_logger.critical(f"FATAL: Startup Diagnostics Failed:\n{err_report}")
            raise RuntimeError(f"Application failed fail-fast startup validation: {len(errors)} critical errors.")

        app_logger.info("🚀 All Startup Diagnostics Passed Successfully! Application ready.")
        return True
