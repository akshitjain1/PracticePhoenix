from datetime import date, timedelta
from app.repositories.history_repository import HistoryRepository


class StatisticsService:

    def __init__(self):
        self.history_repo = HistoryRepository()

    def calculate_streaks(self) -> dict:
        dates = self.history_repo.get_study_dates()
        all_briefs = self.history_repo.get_all_briefs()
        if not dates:
            return {
                "current_streak": 0,
                "longest_streak": 0,
                "total_days": 0,
                "total_briefs": len(all_briefs),
            }

        longest = 1
        curr_run = 1
        for i in range(1, len(dates)):
            if dates[i] == dates[i - 1] + timedelta(days=1):
                curr_run += 1
                if curr_run > longest:
                    longest = curr_run
            else:
                curr_run = 1

        today = date.today()
        latest_date = dates[-1]
        if latest_date < today - timedelta(days=1):
            current = 0
        else:
            current = 1
            idx = len(dates) - 1
            while idx > 0:
                if dates[idx - 1] == dates[idx] - timedelta(days=1):
                    current += 1
                    idx -= 1
                else:
                    break

        return {
            "current_streak": current,
            "longest_streak": longest,
            "total_days": len(dates),
            "total_briefs": len(all_briefs),
        }

    def get_stats_summary(self) -> str:
        stats = self.calculate_streaks()
        return (
            "📈 *Platform Analytics & Activity Statistics*\n\n"
            f"📚 *Total Briefs Generated*: {stats['total_briefs']}\n"
            f"📅 *Total Study Days*: {stats['total_days']} unique days\n"
            f"🔥 *Current Streak*: {stats['current_streak']} consecutive days\n"
            f"🏆 *Longest Streak*: {stats['longest_streak']} consecutive days"
        )

    def get_streak_summary(self) -> str:
        stats = self.calculate_streaks()
        if stats["current_streak"] > 0:
            status = "🚀 Keep up the momentum!"
        else:
            status = "⚡ Start your study streak today with `/daily`!"
        return (
            "🔥 *Daily Study Streak Report*\n\n"
            f"⚡ *Current Streak*: {stats['current_streak']} days\n"
            f"🏆 *Longest Streak*: {stats['longest_streak']} days\n\n"
            f"_{status}_"
        )
