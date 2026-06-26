from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from telegram.ext import Application
from app.config.settings import settings
from app.scheduler.telegram_jobs import morning_broadcast_job
from app.utils.logger import app_logger


class SchedulerService:

    def __init__(self, bot_app: Application | None = None):
        self.bot_app = bot_app
        self.scheduler = AsyncIOScheduler(timezone=settings.TIMEZONE)

    def configure_jobs(self):
        send_time = settings.SEND_TIME.split(":")
        hour = int(send_time[0])
        minute = int(send_time[1]) if len(send_time) > 1 else 0

        trigger = CronTrigger(
            hour=hour,
            minute=minute,
            timezone=settings.TIMEZONE
        )

        self.scheduler.add_job(
            morning_broadcast_job,
            trigger=trigger,
            kwargs={"bot_app": self.bot_app},
            id="morning_brief_job",
            replace_existing=True
        )
        app_logger.info(
            f"Configured morning_brief_job trigger for {hour:02d}:{minute:02d} {settings.TIMEZONE}"
        )

    def start(self):
        self.configure_jobs()
        self.scheduler.start()
        app_logger.info("SchedulerService started.")

    def shutdown(self):
        self.scheduler.shutdown()
        app_logger.info("SchedulerService shutdown.")
