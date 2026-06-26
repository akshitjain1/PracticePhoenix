from app.repositories.curriculum_repository import CurriculumRepository
from app.repositories.progress_repository import ProgressRepository

CATEGORIES = [
    "communication",
    "operating_systems",
    "dbms",
    "computer_networks",
    "linux",
    "backend",
    "ai_engineering",
    "dsa",
    "interview_preparation",
]


class ProgressService:

    def __init__(self):
        self.curriculum_repo = CurriculumRepository()
        self.progress_repo = ProgressRepository()

    def calculate_completion_metrics(self) -> dict:
        progress_map = self.progress_repo.get_all_progress()
        metrics = {}
        total_topics_all = 0
        completed_topics_all = 0

        for cat in CATEGORIES:
            try:
                assets = self.curriculum_repo.load_category(cat)
                total = len(assets)
            except Exception:
                total = 0

            current_idx = progress_map.get(cat, 0)
            completed = min(current_idx, total) if total > 0 else 0
            pct = round((completed / total) * 100, 1) if total > 0 else 0.0
            remaining = max(0, total - completed)

            metrics[cat] = {
                "total": total,
                "completed": completed,
                "current_index": current_idx,
                "percentage": pct,
                "remaining": remaining,
            }
            total_topics_all += total
            completed_topics_all += completed

        overall_pct = (
            round((completed_topics_all / total_topics_all) * 100, 1)
            if total_topics_all > 0
            else 0.0
        )
        return {
            "categories": metrics,
            "overall_completed": completed_topics_all,
            "overall_total": total_topics_all,
            "overall_percentage": overall_pct,
        }

    def get_progress_summary(self) -> str:
        data = self.calculate_completion_metrics()
        lines = [
            f"📊 *Curriculum Completion Overview*: {data['overall_completed']}/{data['overall_total']} lessons ({data['overall_percentage']}%)\n"
        ]

        for cat, info in data["categories"].items():
            disp_name = cat.replace("_", " ").title()
            bar_len = int(info["percentage"] // 10)
            bar = "█" * bar_len + "░" * (10 - bar_len)
            lines.append(
                f"• *{disp_name}*: {info['completed']}/{info['total']} ({info['percentage']}%)\n  `[{bar}]`"
            )

        return "\n".join(lines)

    def get_roadmap_summary(self) -> str:
        data = self.calculate_completion_metrics()
        remaining_total = data["overall_total"] - data["overall_completed"]
        est_days = remaining_total

        lines = [
            "🗺️ *Remaining Curriculum Roadmap*\n",
            f"🎯 *Total Remaining Lessons*: {remaining_total}",
            f"⏱️ *Estimated Days to Complete*: ~{est_days} days\n"
        ]

        for cat, info in data["categories"].items():
            if info["remaining"] > 0:
                disp = cat.replace("_", " ").title()
                lines.append(f"• *{disp}*: {info['remaining']} lessons remaining")

        if remaining_total == 0:
            lines.append("\n🎉 *Congratulations! You have completed 100% of the core curriculum!*")

        return "\n".join(lines)
