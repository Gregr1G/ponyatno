from sqlalchemy import ForeignKey, types

from database import Base
from sqlalchemy.orm import Mapped, mapped_column

class Invite(Base):
    __tablename__ = "invites"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str]
    admin_status: Mapped[bool]
    inviter_id: Mapped[types.Uuid | None] = mapped_column(types.Uuid, ForeignKey("user.id"))
    user_id: Mapped[types.Uuid | None] = mapped_column(types.Uuid, ForeignKey("user.id"))