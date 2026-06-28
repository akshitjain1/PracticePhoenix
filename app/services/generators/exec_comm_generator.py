from app.ai.schemas.daily_schema import ExecutiveCommunication, VocabularyWord
from app.services.generators.base_generator import BaseGenerator


class ExecutiveCommunicationGenerator(BaseGenerator[ExecutiveCommunication]):

    def __init__(self):
        super().__init__("exec_comm.md", ExecutiveCommunication)

    def run(self, topic: str = None) -> ExecutiveCommunication:
        fallback = ExecutiveCommunication(
            vocabulary=[
                VocabularyWord(
                    word="Resilient",
                    pronunciation="ri-zil-yuhnt",
                    meaning="Able to withstand or recover quickly from difficult conditions",
                    synonyms=["robust", "tough"],
                    antonyms=["fragile"],
                    examples=["Designing resilient distributed architectures."]
                )
            ],
            professional_phrase=f"Let's align on {topic or 'system availability'}.",
            communication_principle="Always communicate partial degradation transparently.",
            interview_sentence="We built a resilient messaging pipeline to handle unexpected traffic spikes.",
            daily_usage_challenge="Incorporate the word 'resilient' into your standup or code review today."
        )
        kwargs = {"topic": topic} if topic else {}
        return self.generate(fallback, **kwargs)
