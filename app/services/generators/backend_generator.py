from app.ai.schemas.daily_schema import BackendSection
from app.services.generators.base_generator import BaseGenerator


class BackendGenerator(BaseGenerator[BackendSection]):

    def __init__(self):
        super().__init__("backend.md", BackendSection)

    def run(self, topic: str) -> BackendSection:
        fallback = BackendSection(
            topic=topic,
            question=f"How do you architect and scale {topic} in production?",
            answer="Detailed architectural explanation currently unavailable due to AI provider timeout."
        )
        return self.generate(fallback, topic=topic)
