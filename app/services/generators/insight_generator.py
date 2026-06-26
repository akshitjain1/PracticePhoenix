from app.ai.schemas.daily_schema import EngineeringInsight
from app.services.generators.base_generator import BaseGenerator


class EngineeringInsightGenerator(BaseGenerator[EngineeringInsight]):

    def __init__(self):
        super().__init__("engineering_insight.md", EngineeringInsight)

    def run(self, topic: str) -> EngineeringInsight:
        fallback = EngineeringInsight(
            title=topic,
            description=f"Understanding {topic} is essential for building fault-tolerant backend systems."
        )
        return self.generate(fallback, topic=topic)
