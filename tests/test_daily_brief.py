import json
import pytest
from app.database.init_db import initialize_database
from app.services.curriculum_service import CurriculumService
from app.ai.response_parser import ResponseParser
from app.ai.formatter import TelegramFormatter
from app.ai.providers.provider_factory import ProviderFactory
from app.ai.schemas.daily_schema import DailyBrief


@pytest.fixture(autouse=True)
def setup_db():
    initialize_database()


def test_curriculum_service():
    service = CurriculumService()
    topics = service.get_today_topics()
    
    assert "operating_systems" in topics
    assert "dbms" in topics
    assert "computer_networks" in topics
    assert isinstance(topics["operating_systems"], str)


def test_response_parser_and_formatter():
    mock_json = {
        "executive_communication": {
            "vocabulary": [
                {
                    "word": "Epistemic",
                    "pronunciation": "ep-ih-stem-ik",
                    "meaning": "Relating to knowledge or validation",
                    "synonyms": ["cognitive"],
                    "antonyms": ["ignorant"],
                    "examples": ["Epistemic uncertainty in models."]
                }
            ],
            "professional_phrase": "Let's align on the architectural runway.",
            "communication_principle": "Be concise and structured."
        },
        "operating_systems": {
            "topic": "Mutex",
            "interview_question": "What is a mutex?",
            "why_interviewer_asks": "To test concurrency knowledge.",
            "ideal_answer": "Mutual exclusion locking mechanism.",
            "engineering_explanation": "Prevents race conditions in critical sections.",
            "real_world_example": "Database row lock.",
            "follow_up_questions": ["What is priority inversion?"]
        },
        "dbms": {
            "topic": "ACID",
            "interview_question": "Explain ACID properties.",
            "why_interviewer_asks": "Core transaction concept.",
            "ideal_answer": "Atomicity, Consistency, Isolation, Durability.",
            "engineering_explanation": "Guarantees reliable database transactions.",
            "real_world_example": "Bank fund transfer.",
            "follow_up_questions": ["Difference between serializable and read committed?"]
        },
        "computer_networks": {
            "topic": "TCP",
            "interview_question": "Explain 3-way handshake.",
            "why_interviewer_asks": "To check transport layer understanding.",
            "ideal_answer": "SYN, SYN-ACK, ACK.",
            "engineering_explanation": "Establishes reliable connection sequence numbers.",
            "real_world_example": "Establishing HTTP connection.",
            "follow_up_questions": ["What is SYN flood?"]
        },
        "backend": {
            "topic": "FastAPI",
            "question": "How does FastAPI handle async?",
            "answer": "Using Starlette and anyio event loop."
        },
        "ai_engineering": {
            "topic": "RAG",
            "question": "What is RAG?",
            "answer": "Retrieval-Augmented Generation."
        },
        "dsa": {
            "problem": "Two Sum",
            "pattern": "Hash Map",
            "complexity": "O(n)"
        },
        "engineering_insight": {
            "title": "Idempotency",
            "description": "Operations that can be applied multiple times without changing the result beyond the initial application."
        }
    }
    
    raw_text = f"```json\n{json.dumps(mock_json)}\n```"
    parser = ResponseParser()
    brief = parser.parse(raw_text)
    
    assert isinstance(brief, DailyBrief)
    assert brief.operating_systems.topic == "Mutex"
    
    formatter = TelegramFormatter()
    formatted_msg = formatter.format(brief)
    assert "🚀 *Daily Preparation Brief*" in formatted_msg
    assert "*Topic:* Mutex" in formatted_msg


def test_provider_factory():
    provider = ProviderFactory.get_provider()
    assert hasattr(provider, "generate")
