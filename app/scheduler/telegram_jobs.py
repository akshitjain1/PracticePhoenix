from telegram.ext import Application
from app.scheduler.job_runner import JobRunner
from app.utils.logger import app_logger


async def morning_broadcast_job(bot_app: Application | None = None):
    app_logger.info("APScheduler triggered morning_broadcast_job callback.")
    runner = JobRunner()
    await runner.run_morning_brief(bot_app)
