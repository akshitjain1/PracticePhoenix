from app.ai.schemas.daily_schema import ReadAloudSection, PronunciationWord
from app.services.generators.base_generator import BaseGenerator


class ReadAloudGenerator(BaseGenerator[ReadAloudSection]):

    def __init__(self):
        super().__init__("read_aloud.md", ReadAloudSection)

    def run(self, topic: str = "Distributed Systems") -> ReadAloudSection:
        fallback = ReadAloudSection(
            paragraph=f"When designing scalable {topic}, maintaining data consistency across partitioned replicas requires sophisticated consensus protocols. Engineers must constantly balance write latency against strict serializability guarantees under adverse network conditions.",
            pronunciation_words=[
                PronunciationWord(word="Consensus", pronunciation="kuhn-SEN-suhs"),
                PronunciationWord(word="Partitioned", pronunciation="par-TISH-uhnd"),
                PronunciationWord(word="Serializability", pronunciation="seer-ee-uh-lyze-uh-BIL-ih-tee"),
                PronunciationWord(word="Protocols", pronunciation="PROH-tuh-kohlz"),
                PronunciationWord(word="Adverse", pronunciation="AD-vurs")
            ],
            speaking_challenge="Read the paragraph aloud twice at steady presentation pace without stumbling over multisyllabic architectural terms."
        )
        return self.generate(fallback, topic=topic)
