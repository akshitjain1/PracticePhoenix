from sqlalchemy import Column, Integer, String
from app.database.models import Base


class CurriculumProgress(Base):
    __tablename__ = "curriculum_progress"

    id = Column(Integer, primary_key=True)

    category = Column(String(100), unique=True, nullable=False)

    current_index = Column(Integer, default=0)