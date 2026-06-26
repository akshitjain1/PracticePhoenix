from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime
from app.database.models import Base


class UserActivity(Base):

    __tablename__ = "user_activity"

    id = Column(Integer, primary_key=True)
    event_type = Column(String(50), index=True)
    details = Column(String(255), nullable=True)
    recorded_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
