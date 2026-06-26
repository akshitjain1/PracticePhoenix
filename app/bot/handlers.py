from io import BytesIO
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes
from app.services.daily_service import DailyService
from app.services.history_service import HistoryService
from app.services.search_service import SearchService
from app.services.progress_service import ProgressService
from app.services.statistics_service import StatisticsService
from app.services.analytics_service import AnalyticsService
from app.services.activity_service import ActivityService
from app.services.interview_service import InterviewService
from app.services.health_service import HealthService
from app.ai.formatter import TelegramFormatter
from app.utils.logger import app_logger


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🚀 *Akshit AI Preparation Bot*

Welcome!

This bot will automatically generate your daily preparation brief covering:

• Executive Communication
• Core CS
• AI Engineering
• Backend Engineering
• Engineering Thinking
• DSA
• Interview Preparation
• Daily Revision

Use /help to see available commands.
"""

    await update.message.reply_text(
        text,
        parse_mode=ParseMode.MARKDOWN,
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
Available Commands

/start - Start the bot
/help - Help guide
/test - Test bot status
/health - Live diagnostic system status
/daily - Generate daily study brief
/history - View recent study briefs
/search <keyword> - Search lessons by keyword
/topic <topic> - Retrieve latest lesson on topic
/export - Export complete study history
/progress - Curriculum completion overview
/stats - Activity and volume analytics
/streak - Consecutive study streak report
/weaknesses - Ranked category weaknesses
/roadmap - Remaining curriculum timeline
/grill-me [category] - Start AI interview session
/stop-grill - End active interview session
/score - Check live interview evaluation average
/hint - Get hint for active interview question
/skip - Skip active interview question
"""

    await update.message.reply_text(
        text,
        parse_mode=ParseMode.MARKDOWN,
    )


async def test_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "✅ Bot is running successfully."
    )


async def health_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    service = HealthService()
    await update.message.reply_text(service.get_health_summary(), parse_mode=ParseMode.MARKDOWN)


async def daily_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "⚡ Generating today's preparation brief..."
    )

    try:
        ActivityService().log_interaction("daily_brief_generated", "manual")
        service = DailyService()
        brief = service.generate_daily_brief()

        formatter = TelegramFormatter()
        response = formatter.format(brief)

        await update.message.reply_text(
            response,
            parse_mode=ParseMode.MARKDOWN,
        )
    except Exception as e:
        app_logger.error(f"Error generating daily brief: {e}")
        await update.message.reply_text(
            "❌ Failed to generate daily brief. Please try again later."
        )


async def history_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ActivityService().log_interaction("lesson_viewed", "history_archive")
    service = HistoryService()
    response = service.get_recent_briefs_text()
    await update.message.reply_text(response, parse_mode=ParseMode.MARKDOWN)


async def search_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kw = " ".join(context.args) if context.args else ""
    ActivityService().log_interaction("search_executed", kw)
    service = SearchService()
    response = service.search_keyword(kw)
    await update.message.reply_text(response, parse_mode=ParseMode.MARKDOWN)


async def topic_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tp = " ".join(context.args) if context.args else ""
    ActivityService().log_interaction("topic_reopened", tp)
    service = SearchService()
    response = service.find_topic(tp)
    await update.message.reply_text(response, parse_mode=ParseMode.MARKDOWN)


async def export_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📦 Generating Markdown study history export...")
    try:
        ActivityService().log_interaction("export_generated", "markdown")
        service = HistoryService()
        md_content = service.export_history("md")
        file_obj = BytesIO(md_content.encode("utf-8"))
        file_obj.name = "daily_ai_preparation_history.md"
        await update.message.reply_document(
            document=file_obj,
            caption="📚 Here is your complete study history export."
        )
    except Exception as e:
        app_logger.error(f"Export failed: {e}")
        await update.message.reply_text("❌ Failed to generate export.")


async def progress_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    service = ProgressService()
    await update.message.reply_text(service.get_progress_summary(), parse_mode=ParseMode.MARKDOWN)


async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    service = StatisticsService()
    await update.message.reply_text(service.get_stats_summary(), parse_mode=ParseMode.MARKDOWN)


async def streak_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    service = StatisticsService()
    await update.message.reply_text(service.get_streak_summary(), parse_mode=ParseMode.MARKDOWN)


async def weaknesses_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    service = AnalyticsService()
    await update.message.reply_text(service.get_weaknesses_summary(), parse_mode=ParseMode.MARKDOWN)


async def roadmap_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    service = ProgressService()
    await update.message.reply_text(service.get_roadmap_summary(), parse_mode=ParseMode.MARKDOWN)


async def grill_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cat = context.args[0] if context.args else "general"
    user_id = str(update.effective_user.id if update.effective_user else update.effective_chat.id)
    srv = InterviewService()
    response = srv.start_interview(user_id, cat)
    await update.message.reply_text(response, parse_mode=ParseMode.MARKDOWN)


async def stop_grill_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id if update.effective_user else update.effective_chat.id)
    srv = InterviewService()
    response = srv.stop_interview(user_id)
    await update.message.reply_text(response, parse_mode=ParseMode.MARKDOWN)


async def score_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id if update.effective_user else update.effective_chat.id)
    srv = InterviewService()
    response = srv.get_current_score(user_id)
    await update.message.reply_text(response, parse_mode=ParseMode.MARKDOWN)


async def hint_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id if update.effective_user else update.effective_chat.id)
    srv = InterviewService()
    response = srv.get_hint(user_id)
    await update.message.reply_text(response, parse_mode=ParseMode.MARKDOWN)


async def skip_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id if update.effective_user else update.effective_chat.id)
    srv = InterviewService()
    response = srv.skip_question(user_id)
    await update.message.reply_text(response, parse_mode=ParseMode.MARKDOWN)


async def answer_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
    user_id = str(update.effective_user.id if update.effective_user else update.effective_chat.id)
    text = update.message.text
    srv = InterviewService()
    response = srv.process_answer(user_id, text)
    if response:
        await update.message.reply_text(response, parse_mode=ParseMode.MARKDOWN)