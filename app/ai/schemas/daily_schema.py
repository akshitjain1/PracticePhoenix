from pydantic import BaseModel
from typing import List


class VocabularyWord(BaseModel):
    word: str
    pronunciation: str
    meaning: str
    synonyms: List[str]
    antonyms: List[str]
    examples: List[str]


class ExecutiveCommunication(BaseModel):
    vocabulary: List[VocabularyWord]
    professional_phrase: str
    communication_principle: str


class CSSection(BaseModel):
    topic: str
    interview_question: str
    why_interviewer_asks: str
    ideal_answer: str
    engineering_explanation: str
    real_world_example: str
    follow_up_questions: List[str]


class BackendSection(BaseModel):
    topic: str
    question: str
    answer: str


class AISection(BaseModel):
    topic: str
    question: str
    answer: str


class DSASection(BaseModel):
    problem: str
    pattern: str
    complexity: str


class EngineeringInsight(BaseModel):
    title: str
    description: str


class DailyBrief(BaseModel):

    executive_communication: ExecutiveCommunication

    operating_systems: CSSection

    dbms: CSSection

    computer_networks: CSSection

    backend: BackendSection

    ai_engineering: AISection

    dsa: DSASection

    engineering_insight: EngineeringInsight

    personal_coaching: str = ""