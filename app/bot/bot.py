from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from app.bot.handlers import (
    start_command,
    help_command,
    test_command,
    health_command,
    daily_command,
    history_command,
    search_command,
    topic_command,
    export_command,
    progress_command,
    stats_command,
    streak_command,
    weaknesses_command,
    roadmap_command,
    grill_command,
    stop_grill_command,
    score_command,
    hint_command,
    skip_command,
    answer_message_handler,
)
from app.config.settings import settings
from app.scheduler.scheduler_service import SchedulerService
from app.utils.logger import app_logger


class TelegramBot:

    def __init__(self):
        self.application = (
            Application.builder()
            .token(settings.TELEGRAM_BOT_TOKEN)
            .build()
        )
        self.scheduler_service = SchedulerService(self.application)

    def register_handlers(self):
        self.application.add_handler(
            CommandHandler("start", start_command)
        )
        self.application.add_handler(
            CommandHandler("help", help_command)
        )
        self.application.add_handler(
            CommandHandler("test", test_command)
        )
        self.application.add_handler(
            CommandHandler("health", health_command)
        )
        self.application.add_handler(
            CommandHandler("daily", daily_command)
        )
        self.application.add_handler(
            CommandHandler("history", history_command)
        )
        self.application.add_handler(
            CommandHandler("search", search_command)
        )
        self.application.add_handler(
            CommandHandler("topic", topic_command)
        )
        self.application.add_handler(
            CommandHandler("export", export_command)
        )
        self.application.add_handler(
            CommandHandler("progress", progress_command)
        )
        self.application.add_handler(
            CommandHandler("stats", stats_command)
        )
        self.application.add_handler(
            CommandHandler("streak", streak_command)
        )
        self.application.add_handler(
            CommandHandler("weaknesses", weaknesses_command)
        )
        self.application.add_handler(
            CommandHandler("roadmap", roadmap_command)
        )
        self.application.add_handler(
            CommandHandler("grill-me", grill_command)
        )
        self.application.add_handler(
            CommandHandler("stop-grill", stop_grill_command)
        )
        self.application.add_handler(
            CommandHandler("score", score_command)
        )
        self.application.add_handler(
            CommandHandler("hint", hint_command)
        )
        self.application.add_handler(
            CommandHandler("skip", skip_command)
        )
        self.application.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, answer_message_handler)
        )

    def run(self):
        self.register_handlers()
        app_logger.info("Starting automated daily SchedulerService...")
        self.scheduler_service.start()

        app_logger.info("Telegram Bot Started")
        try:
            self.application.run_polling()
        finally:
            app_logger.info("Initiating Graceful Shutdown sequence...")
            self.scheduler_service.stop()
            app_logger.info("✓ SchedulerService stopped safely. Resources released.")