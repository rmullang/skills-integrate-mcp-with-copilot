from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, nullable=False)
    full_name: Optional[str] = None
    hashed_password: Optional[str] = None
    is_admin: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)


# Simple input model for creating users
class UserCreate(SQLModel):
    email: str
    full_name: Optional[str] = None
    password: Optional[str] = None


# Output model
class UserRead(SQLModel):
    id: int
    email: str
    full_name: Optional[str] = None
    is_admin: bool
    created_at: datetime
