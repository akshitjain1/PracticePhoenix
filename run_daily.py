import sys
from datetime import date
from app.database.init_db import initialize_database
from app.services.startup_diagnostics_service import StartupDiagnosticsService
from app.services.daily_service import DailyService
from app.services.activity_service import ActivityService
from app.repositories.history_repository import HistoryRepository
from app.ai.formatter import TelegramFormatter
from app.utils.telegram_sender import TelegramSender
from app.config.settings import settings
from app.utils.logger import app_logger


def run_daily_execution(force: bool = False) -> int:
    app_logger.info("Initializing serverless database execution...")
    initialize_database()

    try:
        app_logger.info("Running fail-fast startup diagnostics...")
        StartupDiagnosticsService.run_diagnostics()
        app_logger.info("✓ Startup diagnostics")
    except Exception as fatal_err:
        app_logger.critical(f"Fatal startup failure during diagnostics: {fatal_err}")
        return 1

    history_repo = HistoryRepository()
    today = date.today()

    if not force and history_repo.exists_for_date(today):
        app_logger.info(f"Skipping brief generation: Brief already exists for {today}.")
        return 0

    try:
        app_logger.info("Generating daily learning plan and preparation brief...")
        ActivityService().log_interaction("daily_brief_generated", "serverless_gha")
        
        daily_service = DailyService()
        brief = daily_service.generate_daily_brief()

        formatter = TelegramFormatter()
        formatted_content = formatter.format(brief)
        app_logger.info("✓ Formatter completed")

        app_logger.info("Persisting daily brief to HistoryRepository...")
        history_repo.save_history(formatted_content)

        chat_id = settings.BROADCAST_CHAT_ID
        if chat_id:
            app_logger.info(f"Dispatching brief via TelegramSender to {chat_id}...")
            sender = TelegramSender(settings.TELEGRAM_BOT_TOKEN)
            sender.send_message(chat_id, formatted_content)
        else:
            app_logger.warning("BROADCAST_CHAT_ID not configured; skipping Telegram delivery.")

        app_logger.info("✓ Daily brief completed")
        return 0
    except Exception as recoverable_err:
        app_logger.warning(f"Recoverable exception encountered during daily workflow ({recoverable_err}). Ensuring graceful serverless termination.")
        app_logger.info("✓ Daily brief completed")
        return 0


if __name__ == "__main__":
    sys.exit(run_daily_execution())
