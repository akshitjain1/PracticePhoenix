from app.repositories.history_repository import HistoryRepository


class SearchService:

    def __init__(self):
        self.repo = HistoryRepository()

    def search_keyword(self, keyword: str, limit: int = 3) -> str:
        if not keyword or not keyword.strip():
            return "⚠️ Please provide a keyword to search. Example: `/search Mutex`"

        kw = keyword.strip()
        records = self.repo.search_by_keyword(kw, limit)
        if not records:
            return f"🔍 No preparation lessons found containing keyword: `{kw}`."

        lines = [f"🔍 *Search Results for '{kw}'* ({len(records)} found)\n"]
        for r in records:
            dt_str = r.generated_at.strftime("%Y-%m-%d")
            match_line = ""
            for line in r.content.split("\n"):
                if kw.lower() in line.lower():
                    match_line = line.strip()
                    break
            snippet = match_line[:120] if match_line else r.content[:120]
            lines.append(f"📅 *{dt_str}*: {snippet}\n")

        return "\n".join(lines)[:4000]

    def find_topic(self, topic: str) -> str:
        if not topic or not topic.strip():
            return "⚠️ Please provide a topic name. Example: `/topic Processes`"

        tp = topic.strip()
        record = self.repo.retrieve_latest_by_topic(tp)
        if not record:
            return f"📭 No historical lesson found covering topic: `{tp}`."

        dt_str = record.generated_at.strftime("%Y-%m-%d")
        return f"🎯 *Latest Lesson on '{tp}'* (from {dt_str})\n\n{record.content[:3500]}"
