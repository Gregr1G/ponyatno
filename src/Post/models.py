import datetime as dt
import enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class PostPrivacy(str, enum.Enum):
    PUBLIC = "PUBLIC"
    FRIENDS = "FRIENDS"


class Post(BaseModel):
    id: Optional[UUID]
    content: str
    created_at: Optional[dt.datetime]
    updated_at: Optional[dt.datetime]
    wall_profile_id: UUID
    profile_id: UUID
    username: Optional[str]
    privacy: PostPrivacy
    comments_count: int = 0