from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings


engine = create_engine(settings.DATABASE_URL.get_secret_value())
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session() -> Generator:
    """Get db session"""
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
