import datetime as dt
import enum
from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel


class PostPrivacy(str, enum.Enum):
    PUBLIC = "PUBLIC"
    FRIENDS = "FRIENDS"


class Post(BaseModel):
    id: UUID
    wall_owner: UUID
    content: str
    media_files: Optional[List[str]]
    created_at: Optional[dt.datetime]
    privacy: PostPrivacy