from app.ai.schemas.daily_schema import CSSection
from app.services.generators.base_generator import BaseGenerator


class CSSectionGenerator(BaseGenerator[CSSection]):

    def __init__(self, template_filename: str):
        super().__init__(template_filename, CSSection)

    def run(self, topic: str) -> CSSection:
        fallback = CSSection(
            topic=topic,
            interview_question=f"Explain core concepts of {topic}.",
            why_interviewer_asks="Testing foundational computer science knowledge.",
            ideal_answer="Structured conceptual response currently unavailable due to network timeout.",
            engineering_explanation="Please verify implementation details manually.",
            real_world_example="Standard production deployment.",
            follow_up_questions=["How does this scale under high load?"]
        )
        return self.generate(fallback, topic=topic)
