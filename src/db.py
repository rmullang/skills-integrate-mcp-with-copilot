import os
from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data.db")

# echo=True helps during development; can be turned off later
engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    """Create database tables."""
    SQLModel.metadata.create_all(engine)


def get_session():
    """Return a new DB session."""
    return Session(engine)
