from app.repositories.revision_repository import RevisionRepository
from app.services.progress_service import ProgressService
from app.services.activity_service import ActivityService


class AnalyticsService:

    def __init__(self):
        self.revision_repo = RevisionRepository()
        self.progress_service = ProgressService()
        self.activity_service = ActivityService()

    def rank_weaknesses(self) -> list:
        pending_map = self.revision_repo.get_pending_counts()
        progress_data = self.progress_service.calculate_completion_metrics()["categories"]

        rankings = []
        for cat, info in progress_data.items():
            pending = pending_map.get(cat, 0)
            score = (pending * 2) + info["remaining"]
            rankings.append({
                "category": cat,
                "pending_revisions": pending,
                "remaining_lessons": info["remaining"],
                "completion_pct": info["percentage"],
                "weakness_score": score,
            })

        rankings.sort(key=lambda x: x["weakness_score"], reverse=True)
        return rankings

    def get_weaknesses_summary(self) -> str:
        ranked = self.rank_weaknesses()
        activity = self.activity_service.get_activity_summary()
        lines = [
            "🎯 *Domain Weaknesses & Revision Focus Ranking*\n",
            f"_Derived across {activity['total_interactions']} learning interactions:_\n"
        ]

        for idx, item in enumerate(ranked[:5], start=1):
            disp = item["category"].replace("_", " ").title()
            lines.append(
                f"{idx}. *{disp}*\n"
                f"   • Queued Revisions: {item['pending_revisions']}\n"
                f"   • Remaining Lessons: {item['remaining_lessons']} ({item['completion_pct']}% complete)"
            )

        return "\n".join(lines)
