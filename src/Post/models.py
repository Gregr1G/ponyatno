from datetime import datetime
from typing import List

from sqlalchemy import ForeignKey, types, DateTime

from src.Post.schemas import PostPrivacy
from pytz import timezone
from database import Base
from sqlalchemy.orm import Mapped, mapped_column


class Invite(Base):
    __tablename__ = "post"

    id: Mapped[types.Uuid] = mapped_column(primary_key=True)
    wall_owner: Mapped[types.Uuid] = mapped_column(types.Uuid, ForeignKey("user.id"))
    content: Mapped[str]
    media_files: Mapped[List[str] | None]
    created_at: Mapped[DateTime] = mapped_column(default=datetime.now(timezone('UTC')))
    privacy: Mapped[PostPrivacy] = mapped_column(server_default=f"{PostPrivacy.PUBLIC.value}")
