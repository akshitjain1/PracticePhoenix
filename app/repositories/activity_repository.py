from datetime import datetime, timezone
from typing import List, Dict
from sqlalchemy import select, func
from app.database.database import SessionLocal
from app.models.activity import UserActivity


class ActivityRepository:

    def record_event(self, event_type: str, details: str = "") -> UserActivity:
        with SessionLocal() as session:
            event = UserActivity(
                event_type=event_type,
                details=details[:255] if details else "",
                recorded_at=datetime.now(timezone.utc)
            )
            session.add(event)
            session.commit()
            session.refresh(event)
            return event

    def get_event_counts(self) -> Dict[str, int]:
        with SessionLocal() as session:
            records = session.execute(
                select(UserActivity.event_type, func.count(UserActivity.id))
                .group_by(UserActivity.event_type)
            ).all()
            return {r[0]: r[1] for r in records}

    def get_recent_events(self, limit: int = 20) -> List[UserActivity]:
        with SessionLocal() as session:
            records = session.execute(
                select(UserActivity)
                .order_by(UserActivity.recorded_at.desc())
                .limit(limit)
            ).scalars().all()
            return list(records)
