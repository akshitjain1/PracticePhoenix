from datetime import date
from typing import List, Dict
from sqlalchemy import select, delete, func
from app.database.database import SessionLocal
from app.models.revision import RevisionQueue


class RevisionRepository:

    def schedule_if_not_exists(
        self, category: str, topic: str, revision_date: date, stage: int
    ) -> RevisionQueue:
        with SessionLocal() as session:
            existing = session.execute(
                select(RevisionQueue).where(
                    RevisionQueue.category == category,
                    RevisionQueue.topic == topic,
                    RevisionQueue.stage == stage,
                )
            ).scalar_one_or_none()

            if existing:
                return existing

            new_item = RevisionQueue(
                category=category,
                topic=topic,
                revision_date=revision_date,
                stage=stage,
            )
            session.add(new_item)
            session.commit()
            session.refresh(new_item)
            return new_item

    def get_due_today(self, category: str, target_date: date) -> List[RevisionQueue]:
        with SessionLocal() as session:
            results = session.execute(
                select(RevisionQueue).where(
                    RevisionQueue.category == category,
                    RevisionQueue.revision_date <= target_date,
                )
            ).scalars().all()
            return list(results)

    def remove_by_ids(self, ids: List[int]):
        if not ids:
            return
        with SessionLocal() as session:
            session.execute(delete(RevisionQueue).where(RevisionQueue.id.in_(ids)))
            session.commit()

    def get_pending_counts(self) -> Dict[str, int]:
        with SessionLocal() as session:
            records = session.execute(
                select(RevisionQueue.category, func.count(RevisionQueue.id))
                .group_by(RevisionQueue.category)
            ).all()
            return {r[0]: r[1] for r in records}
