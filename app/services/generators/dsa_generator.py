from app.ai.schemas.daily_schema import DSASection
from app.services.generators.base_generator import BaseGenerator


class DSAGenerator(BaseGenerator[DSASection]):

    def __init__(self):
        super().__init__("dsa.md", DSASection)

    def run(self, topic: str) -> DSASection:
        fallback = DSASection(
            problem=topic,
            pattern="Standard Algorithmic Pattern",
            complexity="Time: O(N) | Space: O(1)"
        )
        return self.generate(fallback, topic=topic)
