from app.ai.schemas.daily_schema import NewsSection
from app.services.generators.base_generator import BaseGenerator


class NewsGenerator(BaseGenerator[NewsSection]):

    def __init__(self):
        super().__init__("news.md", NewsSection)

    def run(self, topic: str = "Cloud & Backend Architecture") -> NewsSection:
        fallback = NewsSection(
            summary=f"Recent breakthroughs in {topic} focus on low-latency microservice orchestration.",
            why_it_matters="Directly impacts system reliability and container resource budgeting under peak traffic.",
            interview_relevance="Frequently explored during Senior Systems Design scalability trade-off discussions."
        )
        return self.generate(fallback, topic=topic)
