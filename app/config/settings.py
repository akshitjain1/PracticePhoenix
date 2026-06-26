from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):

    TELEGRAM_BOT_TOKEN: str

    GROQ_API_KEY: str

    AI_PROVIDER: str = "groq"

    MODEL_NAME: str = "llama-3.3-70b-versatile"

    DATABASE_PATH: str = "data/preparation.db"

    TIMEZONE: str = "Asia/Kolkata"

    SEND_TIME: str = "07:00"

    BROADCAST_CHAT_ID: str = ""

    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()