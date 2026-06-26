from datetime import date
from tenacity import retry, stop_after_attempt, wait_exponential
from telegram.ext import Application
from app.ai.formatter import TelegramFormatter
from app.config.settings import settings
from app.repositories.history_repository import HistoryRepository
from app.services.daily_service import DailyService
from app.services.activity_service import ActivityService
from app.utils.logger import app_logger


class JobRunner:

    def __init__(self):
        self.history_repo = HistoryRepository()
        self.formatter = TelegramFormatter()

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        reraise=True
    )
    async def run_morning_brief(self, bot_app: Application | None = None, force: bool = False) -> str:
        app_logger.info("JobRunner executing scheduled daily brief generation...")
        
        today = date.today()
        if not force and self.history_repo.exists_for_date(today):
            app_logger.info(f"Skipping scheduled brief generation: Brief already generated and recorded for {today}.")
            return "SKIPPED_DUPLICATE"

        ActivityService().log_interaction("daily_brief_generated", "scheduled")
        service = DailyService()
        brief = service.generate_daily_brief()
        formatted_content = self.formatter.format(brief)

        self.history_repo.save_history(formatted_content)
        app_logger.info("Persisted scheduled brief to DailyHistory.")

        chat_id = settings.BROADCAST_CHAT_ID
        if bot_app and chat_id:
            try:
                await bot_app.bot.send_message(
                    chat_id=chat_id,
                    text=formatted_content,
                    parse_mode="Markdown"
                )
                app_logger.info(f"Delivered morning brief to chat {chat_id}.")
            except Exception as e:
                app_logger.error(f"Failed Telegram delivery to chat {chat_id}: {e}")
                raise e
        else:
            app_logger.warning("Telegram delivery skipped (no bot_app or BROADCAST_CHAT_ID).")
        
        return formatted_content
