from app.bot.bot import TelegramBot
from app.database.init_db import initialize_database
from app.services.startup_diagnostics_service import StartupDiagnosticsService
from app.utils.logger import app_logger


def main():
    app_logger.info("Initializing Database...")
    initialize_database()
    app_logger.info("Database Initialized")

    # Fail fast configuration & diagnostic validation
    StartupDiagnosticsService.run_diagnostics()

    bot = TelegramBot()
    app_logger.info("Starting Telegram Bot...")
    bot.run()


if __name__ == "__main__":
    main()