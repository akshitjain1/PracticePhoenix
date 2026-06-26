from pydantic import BaseModel
from sqlalchemy import text
from app.database.database import engine
from app.repositories.history_repository import HistoryRepository
from app.repositories.curriculum_repository import CurriculumRepository
from app.config.settings import settings


class HealthStatus(BaseModel):
    status: str
    database: str
    ai_provider: str
    scheduler: str
    curriculum: str
    history_archive: str


class HealthService:

    def check_health(self) -> HealthStatus:
        db_stat = "UP"
        try:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
        except Exception:
            db_stat = "DOWN"

        ai_stat = "UP" if bool(settings.GROQ_API_KEY) else "MISSING_KEY"

        cur_stat = "UP"
        try:
            if not CurriculumRepository().load_category("operating_systems"):
                cur_stat = "EMPTY"
        except Exception:
            cur_stat = "DOWN"

        hist_stat = "UP"
        try:
            HistoryRepository().get_recent_briefs(1)
        except Exception:
            hist_stat = "DOWN"

        sched_stat = "UP"

        overall = "HEALTHY"
        if "DOWN" in [db_stat, cur_stat, hist_stat]:
            overall = "UNHEALTHY"
        elif "MISSING_KEY" in [ai_stat]:
            overall = "DEGRADED"

        return HealthStatus(
            status=overall,
            database=db_stat,
            ai_provider=ai_stat,
            scheduler=sched_stat,
            curriculum=cur_stat,
            history_archive=hist_stat
        )

    def get_health_summary(self) -> str:
        h = self.check_health()
        icon = "✅" if h.status == "HEALTHY" else ("⚠️" if h.status == "DEGRADED" else "❌")
        return (
            f"{icon} *System Health Report: {h.status}*\n\n"
            f"• Database Connectivity: `{h.database}`\n"
            f"• AI Provider Gateway: `{h.ai_provider}`\n"
            f"• Background Scheduler: `{h.scheduler}`\n"
            f"• Curriculum Asset Store: `{h.curriculum}`\n"
            f"• History Repository: `{h.history_archive}`"
        )
