from typing import Dict
from sqlalchemy import select
from app.database.database import SessionLocal
from app.models.progress import CurriculumProgress


class ProgressRepository:

    def get_index(self, category: str) -> int:
        with SessionLocal() as session:
            result = session.execute(
                select(CurriculumProgress).where(
                    CurriculumProgress.category == category
                )
            ).scalar_one_or_none()

            if result is None:
                result = CurriculumProgress(
                    category=category,
                    current_index=0
                )
                session.add(result)
                session.commit()
                session.refresh(result)

            return result.current_index

    def increment(self, category: str):
        with SessionLocal() as session:
            result = session.execute(
                select(CurriculumProgress).where(
                    CurriculumProgress.category == category
                )
            ).scalar_one()

            result.current_index += 1
            session.commit()

    def get_all_progress(self) -> Dict[str, int]:
        with SessionLocal() as session:
            records = session.execute(select(CurriculumProgress)).scalars().all()
            return {r.category: r.current_index for r in records}