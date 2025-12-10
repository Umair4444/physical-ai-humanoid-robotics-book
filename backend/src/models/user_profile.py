from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel, JSON, Column
from pydantic import BaseModel
from typing import Dict, Any


class UserProfileBase(SQLModel):
    auth_provider_id: str = Field(index=True)
    full_name: Optional[str] = None
    email: str = Field(unique=True, index=True)
    password_hash: str # Added for storing hashed passwords
    registration_date: datetime = Field(default_factory=datetime.utcnow)
    last_login_date: datetime = Field(default_factory=datetime.utcnow)
    profile_data: Dict[str, Any] = Field(default_factory=dict, sa_column=Column(JSON))


class UserProfile(UserProfileBase, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)


class UserProfileCreate(BaseModel): # Changed from UserProfileBase
    email: str
    password: str
    full_name: Optional[str] = None
    profile_data: Optional[Dict[str, Any]] = None


class UserProfileUpdate(BaseModel):
    full_name: Optional[str] = None
    profile_data: Optional[Dict[str, Any]] = None

