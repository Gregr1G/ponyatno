from uuid import uuid4, UUID
from sqlalchemy import ForeignKey, types, DateTime, func
import datetime
from database import Base
from sqlalchemy.orm import Mapped, mapped_column

from src.Post.schemas import PostsPrivacy


class Post(Base):
    __tablename__ = "post"

    id: Mapped[UUID] = mapped_column(primary_key=True, server_default=func.gen_random_uuid())
    post_owner: Mapped[types.Uuid] = mapped_column(types.Uuid, ForeignKey("user.id"))
    content: Mapped[str]
    media_files: Mapped[str]
    created_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    privacy: Mapped[PostsPrivacy] = mapped_column(server_default=f"{PostsPrivacy.PUBLIC.value}")
