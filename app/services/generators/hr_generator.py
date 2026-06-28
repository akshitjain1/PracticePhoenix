from app.ai.schemas.daily_schema import HRSection
from app.services.generators.base_generator import BaseGenerator


class HRGenerator(BaseGenerator[HRSection]):

    def __init__(self):
        super().__init__("hr.md", HRSection)

    def run(self, topic: str = "Technical Leadership") -> HRSection:
        fallback = HRSection(
            behavioral_question=f"Tell me about a time you demonstrated {topic} during a high-stakes engineering project.",
            why_interviewer_asks="Evaluates ownership, technical composure, and communication maturity under tight project timelines.",
            star_framework="Situation: Critical sprint deadline -> Task: Align engineering priorities -> Action: Implemented structured architectural checkpoints -> Result: Delivered on schedule with zero production regressions.",
            sample_answer="During our core payment migration, I established daily technical syncs and automated rollback triggers, ensuring our 12-person team delivered the gateway on schedule with zero downtime.",
            common_mistakes="Focusing exclusively on individual code contributions while omitting team leadership or quantifiable business impact.",
            practice_task="Outline a 4-bullet STAR response detailing a complex technical challenge you personally resolved."
        )
        return self.generate(fallback, topic=topic)
