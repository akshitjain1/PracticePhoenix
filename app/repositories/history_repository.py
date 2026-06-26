from datetime import datetime, timezone, date
from typing import List, Optional
from sqlalchemy import select
from app.database.database import SessionLocal
from app.models.history import DailyHistory


class HistoryRepository:

    def save_history(self, content: str) -> DailyHistory:
        with SessionLocal() as session:
            record = DailyHistory(
                content=content,
                generated_at=datetime.now(timezone.utc)
            )
            session.add(record)
            session.commit()
            session.refresh(record)
            return record

    def get_recent_briefs(self, limit: int = 5) -> List[DailyHistory]:
        with SessionLocal() as session:
            records = session.execute(
                select(DailyHistory)
                .order_by(DailyHistory.generated_at.desc())
                .limit(limit)
            ).scalars().all()
            return list(records)

    def search_by_keyword(self, keyword: str, limit: int = 5) -> List[DailyHistory]:
        with SessionLocal() as session:
            records = session.execute(
                select(DailyHistory)
                .where(DailyHistory.content.ilike(f"%{keyword}%"))
                .order_by(DailyHistory.generated_at.desc())
                .limit(limit)
            ).scalars().all()
            return list(records)

    def retrieve_latest_by_topic(self, topic: str) -> Optional[DailyHistory]:
        with SessionLocal() as session:
            record = session.execute(
                select(DailyHistory)
                .where(DailyHistory.content.ilike(f"%{topic}%"))
                .order_by(DailyHistory.generated_at.desc())
                .limit(1)
            ).scalar_one_or_none()
            return record

    def get_all_briefs(self) -> List[DailyHistory]:
        with SessionLocal() as session:
            records = session.execute(
                select(DailyHistory).order_by(DailyHistory.generated_at.asc())
            ).scalars().all()
            return list(records)

    def get_study_dates(self) -> List[date]:
        with SessionLocal() as session:
            records = session.execute(
                select(DailyHistory.generated_at).order_by(DailyHistory.generated_at.asc())
            ).scalars().all()
            dates = sorted(list({dt.date() for dt in records if dt}))
            return dates

    def exists_for_date(self, target_date: date) -> bool:
        with SessionLocal() as session:
            records = session.execute(
                select(DailyHistory.generated_at)
            ).scalars().all()
            return any(dt.date() == target_date for dt in records if dt)
