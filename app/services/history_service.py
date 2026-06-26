from app.repositories.history_repository import HistoryRepository


class HistoryService:

    def __init__(self):
        self.repo = HistoryRepository()

    def get_recent_briefs_text(self, limit: int = 3) -> str:
        briefs = self.repo.get_recent_briefs(limit)
        if not briefs:
            return "📭 No preparation briefs found in history."

        lines = [f"📜 *Recent {len(briefs)} Daily Preparation Briefs*\n"]
        for b in briefs:
            dt_str = b.generated_at.strftime("%Y-%m-%d %H:%M UTC")
            snippet = b.content[:200].replace("\n", " ") + "..."
            lines.append(f"• *{dt_str}*:\n  _{snippet}_\n")

        return "\n".join(lines)[:4000]

    def export_history(self, format: str = "md") -> str:
        if format != "md":
            raise NotImplementedError(
                f"Export format '{format}' not supported yet. Pluggable design supports adding PDF renderers later."
            )

        briefs = self.repo.get_all_briefs()
        if not briefs:
            return "# Daily AI Preparation Platform - Study History\n\nNo historical records found."

        doc = [
            "# Daily AI Preparation Platform - Complete Study History\n",
            f"**Total Briefs Recorded**: {len(briefs)}\n\n---\n"
        ]
        for b in briefs:
            dt_str = b.generated_at.strftime("%Y-%m-%d %H:%M:%S UTC")
            doc.append(f"## Brief Generated: {dt_str}\n\n{b.content}\n\n---\n")

        return "\n".join(doc)
