import datetime as dt
import enum
from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel


class PostsPrivacy(str, enum.Enum):
    PUBLIC = "PUBLIC"
    FRIENDS = "FRIENDS"


class PostSchema(BaseModel):
    id: UUID
    wall_owner: UUID
    content: str
    media_files: Optional[List[str]]
    created_at: Optional[dt.datetime]
    privacy: PostsPrivacy