from pathlib import Path

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from app.config.settings import settings


db_path = Path(settings.DATABASE_PATH)

db_path.parent.mkdir(parents=True, exist_ok=True)

engine = create_engine(
    f"sqlite:///{db_path}",
    future=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)