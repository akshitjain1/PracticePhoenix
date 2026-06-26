from app.database.database import engine
from app.database.models import Base

import app.models.progress
import app.models.history
import app.models.revision
import app.models.activity
import app.models.interview


def initialize_database():
    Base.metadata.create_all(bind=engine)