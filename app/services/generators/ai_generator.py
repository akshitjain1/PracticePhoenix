from app.ai.schemas.daily_schema import AISection
from app.services.generators.base_generator import BaseGenerator


class AIEngineeringGenerator(BaseGenerator[AISection]):

    def __init__(self):
        super().__init__("ai_engineering.md", AISection)

    def run(self, topic: str) -> AISection:
        fallback = AISection(
            topic=topic,
            question=f"What are key architectural considerations when implementing {topic}?",
            answer="AI engineering deep-dive currently unavailable due to timeout."
        )
        return self.generate(fallback, topic=topic)
