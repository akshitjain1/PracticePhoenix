import pytest
from app.utils.telegram_sender import TelegramSender
from run_daily import run_daily_execution
from app.database.init_db import initialize_database


@pytest.fixture(autouse=True)
def setup_db():
    initialize_database()


def test_telegram_sender_mock_dispatch():
    sender = TelegramSender(token="mock_ci_token")
    res = sender.send_message(chat_id="12345", text="Test brief content")
    assert res is True


def test_run_daily_execution_flow():
    exit_code = run_daily_execution(force=True)
    assert exit_code == 0

    exit_code_skip = run_daily_execution(force=False)
    assert exit_code_skip == 0
