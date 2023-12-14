import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings


DATABASE_URL = os.environ.get('DATABASE_URL')

engine = create_engine(settings.DATABASE_URL.get_secret_value())

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
