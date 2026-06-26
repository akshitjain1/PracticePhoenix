from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date

from app.database.models import Base


class RevisionQueue(Base):

    __tablename__ = "revision_queue"

    id = Column(Integer, primary_key=True)

    category = Column(String(100))

    topic = Column(String(300))

    revision_date = Column(Date)

    stage = Column(Integer)