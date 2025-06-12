from sqlalchemy.orm import Session, declarative_base, sessionmaker
from sqlalchemy import create_engine

DATABASE_CONNECTION_URL = "sqlite:///./database.db"

engine = create_engine(DATABASE_CONNECTION_URL)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#, connect_args={"check_same_thread": False}