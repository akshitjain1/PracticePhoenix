from datetime import datetime, timezone
from sqlalchemy import Column, Integer, DateTime, Text
from app.database.models import Base


class DailyHistory(Base):

    __tablename__ = "daily_history"

    id = Column(Integer, primary_key=True)

    generated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc)
    )

    content = Column(Text)