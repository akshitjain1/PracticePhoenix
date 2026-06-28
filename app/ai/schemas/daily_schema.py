from pydantic import BaseModel, Field
from typing import List, Optional


class WelcomeDashboard(BaseModel):
    day_number: int = 1
    current_streak: int = 1
    curriculum_progress: float = 0.0
    estimated_study_time: int = 25
    difficulty: str = "⭐⭐⭐⭐ (Advanced)"
    todays_focus: str = "System Architecture & Core Engineering"


class NewsSection(BaseModel):
    headline: str = "Latest Software Engineering Update"
    summary: str = "Linux Kernel EEVDF latency-sensitive scheduler optimizations."
    why_it_matters: str = "Drastically reduces tail latency for containerized microservice workloads."
    interview_relevance: str = "Demonstrates deep fluency in CPU preemption during system design rounds."


class PronunciationWord(BaseModel):
    word: str = ""
    pronunciation: str = ""
    ipa: str = ""
    audio_respeaking: str = ""


class ReadAloudSection(BaseModel):
    paragraph: str = "In high-throughput distributed systems, cache stampedes occur when concurrent worker threads simultaneously attempt to recompute an expired key, leading to catastrophic database lock saturation and cascading backend degradation."
    pronunciation_words: List[PronunciationWord] = [
        PronunciationWord(word="Stampede", pronunciation="stam-PEED", ipa="stam-PEED", audio_respeaking="stam-PEED"),
        PronunciationWord(word="Catastrophic", pronunciation="kat-uh-STROF-ik", ipa="kat-uh-STROF-ik", audio_respeaking="kat-uh-STROF-ik"),
        PronunciationWord(word="Degradation", pronunciation="deg-ruh-DAY-shun", ipa="deg-ruh-DAY-shun", audio_respeaking="deg-ruh-DAY-shun")
    ]
    words: Optional[List[PronunciationWord]] = None
    speaking_challenge: str = "Read the paragraph aloud twice at speaking pace without stuttering."
    reading_tips: str = "Maintain a steady pace and emphasize technical nouns clearly."

    def __init__(self, **data):
        super().__init__(**data)
        if self.words is None:
            self.words = self.pronunciation_words


class VocabularyWord(BaseModel):
    word: str = ""
    pronunciation: str = ""
    meaning: str = ""
    synonyms: List[str] = []
    antonyms: List[str] = []
    examples: List[str] = []


class ExecutiveCommunication(BaseModel):
    vocabulary: List[VocabularyWord] = [
        VocabularyWord(word="Idempotency", pronunciation="eye-dem-PO-ten-see", meaning="Property where applying an operation multiple times yields the exact same state.", synonyms=["repeatable"], antonyms=["variable"], examples=["Payment gateways guarantee idempotent API requests."])
    ]
    professional_phrase: str = "Let's ensure our retry pipelines maintain strict idempotency."
    communication_principle: str = "Always communicate degradation transparently."
    interview_sentence: str = "To prevent duplicate orders during retries, I designed the API endpoints to be strictly idempotent."
    daily_usage_challenge: str = "Use the word Idempotency when explaining retry logic in your next code review."
    # Mobile app flat compatibility fields
    pronunciation: str = "eye-dem-PO-ten-see"
    meaning: str = "Property where applying an operation multiple times yields the exact same state."
    business_example: str = "Payment processing webhooks use unique transaction keys to guarantee idempotent charges."
    daily_challenge: str = "Use the word Idempotency when explaining retry logic in your next code review."

    def __init__(self, **data):
        super().__init__(**data)
        if self.vocabulary and isinstance(self.vocabulary, list) and len(self.vocabulary) > 0:
            v = self.vocabulary[0]
            self.pronunciation = v.pronunciation or self.pronunciation
            self.meaning = v.meaning or self.meaning
            if v.examples and len(v.examples) > 0:
                self.business_example = v.examples[0]


class HRSection(BaseModel):
    behavioral_question: str = "Tell me about a time you had to make a critical engineering decision with incomplete data under tight deadlines."
    question: str = "Tell me about a time you had to make a critical engineering decision with incomplete data under tight deadlines."
    why_interviewer_asks: str = "Evaluates risk assessment autonomy, composure, and ownership."
    star_framework: str = "Situation: Latency spikes before launch -> Task: Decide rollback vs fix -> Action: Circuit-breaker fallback + tracing -> Result: Zero downtime."
    sample_answer: str = "When our checkout gateway experienced uncharacterized latency spikes 48 hours before launch, I implemented a circuit-breaker fallback while attaching OpenTelemetry spans, isolating the root cause within 6 hours with zero downtime."
    ideal_answer: str = "When our checkout gateway experienced uncharacterized latency spikes 48 hours before launch, I implemented a circuit-breaker fallback while attaching OpenTelemetry spans, isolating the root cause within 6 hours with zero downtime."
    common_mistakes: str = "Blaming product managers for tight deadlines or failing to quantify business impact."
    practice_task: str = "Write out your own 4-bullet STAR outline for a high-pressure technical decision."

    def __init__(self, **data):
        super().__init__(**data)
        if "question" not in data and "behavioral_question" in data:
            self.question = data["behavioral_question"]
        elif "behavioral_question" not in data and "question" in data:
            self.behavioral_question = data["question"]
        if "ideal_answer" not in data and "sample_answer" in data:
            self.ideal_answer = data["sample_answer"]
        elif "sample_answer" not in data and "ideal_answer" in data:
            self.sample_answer = data["ideal_answer"]


class CSSection(BaseModel):
    topic: str = "Technical Subject"
    definition: str = "Fundamental architectural concept governing reliable systems."
    interview_question: str = "How do you optimize data access patterns under high load?"
    why_interviewer_asks: str = "Evaluates architectural depth."
    ideal_answer: str = "Utilize multi-tiered caching, connection pooling, and asynchronous replication."
    production_example: str = "High-throughput microservices handling millions of requests per minute."
    engineering_explanation: str = "Deep under-the-hood engine details and trade-offs."
    real_world_example: str = "Concrete production usage example."
    common_mistake: str = "Ignoring network serialization overhead and lock contention."
    follow_up_question: str = "How would your design change if network partition frequency doubled?"
    follow_up_questions: List[str] = ["How would your design change if network partition frequency doubled?"]

    def __init__(self, **data):
        super().__init__(**data)
        if not self.definition and self.engineering_explanation:
            self.definition = self.engineering_explanation[:150]
        if not self.production_example and self.real_world_example:
            self.production_example = self.real_world_example
        if not self.follow_up_question and self.follow_up_questions:
            self.follow_up_question = self.follow_up_questions[0]


class BackendSection(BaseModel):
    topic: str = "Distributed Backend Architecture"
    question: str = "How do you handle distributed transactions?"
    interview_question: str = "How do you handle distributed transactions?"
    definition: str = "Mechanisms ensuring ACID properties across multiple independent datastores."
    answer: str = "Use Saga pattern or Two-Phase Commit (2PC) with idempotency keys."
    ideal_answer: str = "Use Saga pattern or Two-Phase Commit (2PC) with idempotency keys."
    production_example: str = "E-commerce order fulfillment orchestrating payment and inventory microservices."
    common_mistake: str = "Using distributed locks across high-latency WAN links."
    follow_up_question: str = "What happens if the orchestrator fails mid-transaction?"

    def __init__(self, **data):
        super().__init__(**data)
        if "interview_question" not in data and "question" in data:
            self.interview_question = data["question"]
        if "ideal_answer" not in data and "answer" in data:
            self.ideal_answer = data["answer"]


class AISection(BaseModel):
    topic: str = "LLM Inference & RAG"
    question: str = "How do you optimize LLM KV Cache memory footprint?"
    interview_question: str = "How do you optimize LLM KV Cache memory footprint?"
    definition: str = "Caching key and value tensors during autoregressive token generation."
    answer: str = "Implement PagedAttention and Multi-Query Attention (MQA) to reduce VRAM fragmentation."
    ideal_answer: str = "Implement PagedAttention and Multi-Query Attention (MQA) to reduce VRAM fragmentation."
    production_example: str = "vLLM inference server serving concurrent chat requests."
    common_mistake: str = "Allocating contiguous VRAM blocks leading to out-of-memory errors."
    follow_up_question: str = "How does quantization impact KV cache accuracy?"

    def __init__(self, **data):
        super().__init__(**data)
        if "interview_question" not in data and "question" in data:
            self.interview_question = data["question"]
        if "ideal_answer" not in data and "answer" in data:
            self.ideal_answer = data["answer"]


class DSASection(BaseModel):
    topic: str = "Dynamic Programming & Graphs"
    problem: str = "Find the shortest path in a weighted graph with negative cycles."
    interview_question: str = "Find the shortest path in a weighted graph with negative cycles."
    definition: str = "Algorithmic technique for computing optimal paths."
    pattern: str = "Bellman-Ford Algorithm dynamic programming relaxation."
    ideal_answer: str = "Use Bellman-Ford algorithm relaxing edges V-1 times."
    complexity: str = "Time: O(V*E) | Space: O(V)"
    production_example: str = "Network routing protocols calculating dynamic link costs."
    common_mistake: str = "Using Dijkstra's algorithm which fails on negative edge weights."
    follow_up_question: str = "How would you detect infinite negative cycles?"

    def __init__(self, **data):
        super().__init__(**data)
        if "interview_question" not in data and "problem" in data:
            self.interview_question = data["problem"]
        if "ideal_answer" not in data and "pattern" in data:
            self.ideal_answer = f"{data['pattern']} ({self.complexity})"
        if "topic" not in data and "problem" in data:
            self.topic = data["problem"][:30] + "..."


class EngineeringInsight(BaseModel):
    title: str = "Principle of Least Privilege"
    description: str = "Systems should operate with the minimal permissions required to accomplish their task."


class DailyBrief(BaseModel):
    welcome_dashboard: WelcomeDashboard = WelcomeDashboard()
    news_section: NewsSection = NewsSection()
    read_aloud_section: ReadAloudSection = ReadAloudSection()
    hr_section: HRSection = HRSection()

    executive_communication: ExecutiveCommunication = ExecutiveCommunication()
    exec_comm_section: Optional[ExecutiveCommunication] = None
    operating_systems: CSSection = CSSection(topic="Operating Systems Virtualization")
    dbms: CSSection = CSSection(topic="Database Isolation Levels & MVCC")
    computer_networks: CSSection = CSSection(topic="TCP 3-Way Handshake & Congestion Control")
    linux: CSSection = CSSection(topic="Linux Kernel Processes & File Descriptors")
    sql: CSSection = CSSection(topic="Advanced Window Functions & Indexing")
    backend: BackendSection = BackendSection()
    ai_engineering: AISection = AISection()
    dsa: DSASection = DSASection()
    system_design: CSSection = CSSection(topic="Consistent Hashing & Replication Strategies")
    engineering_insight: EngineeringInsight = EngineeringInsight()
    personal_coaching: str = "🌟 *Executive Career Mentor Note*: Maintain steady compounding progress every day."

    def __init__(self, **data):
        super().__init__(**data)
        if self.exec_comm_section is None:
            self.exec_comm_section = self.executive_communication