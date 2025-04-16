# app/core/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./immobilier.db"  # à adapter si tu utilises PostgreSQL ou autre

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}  # Spécifique à SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def create_db_and_tables():
    Base.metadata.create_all(bind=engine)