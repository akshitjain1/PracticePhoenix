import pytest
from app.utils.message_chunker import MessageChunker
from app.utils.telegram_sender import TelegramSender
from app.ai.response_parser import ResponseParser
from app.ai.schemas.daily_schema import BackendSection
from app.services.daily_service import DailyService
from app.database.init_db import initialize_database


@pytest.fixture(autouse=True)
def setup_db():
    initialize_database()


def test_message_chunking_under_limit():
    text = "Short text"
    chunks = MessageChunker.chunk_message(text, max_length=4000)
    assert chunks == ["Short text"]


def test_message_chunking_order_and_markdown():
    section1 = "# Section 1\n" + ("A" * 2500)
    section2 = "## Section 2\n" + ("B" * 2500)
    text = f"{section1}\n\n{section2}"

    chunks = MessageChunker.chunk_message(text, max_length=4000)
    assert len(chunks) == 2
    assert chunks[0].startswith("# Section 1")
    assert chunks[1].startswith("## Section 2")


def test_telegram_sender_multiple_chunks():
    sender = TelegramSender(token="mock_ci_token")
    long_text = ("Paragraph 1\n\n" * 400)
    res = sender.send_message(chat_id="12345", text=long_text)
    assert res is True


def test_malformed_json_recovery_and_schema_validation():
    parser = ResponseParser()
    malformed = """```json\n{\n  "topic": "Caching",\n  "question": "Explain Redis?",\n  "answer": "Fast memory cache"\n}```"""
    sec = parser.parse_section(malformed, BackendSection)
    assert sec.topic == "Caching"

    with pytest.raises(ValueError):
        parser.parse_section("{invalid_json: [}", BackendSection)


def test_daily_service_isolation_and_fallback():
    service = DailyService()
    brief = service.generate_daily_brief()
    assert brief.executive_communication is not None
    assert brief.backend is not None
    assert brief.personal_coaching is not None
