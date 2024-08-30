from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped

from config import url


class Base(DeclarativeBase):
    pass

# юзеры
class User(SQLAlchemyBaseUserTableUUID, Base):
    username: Mapped[str | None] # юзернейм
    phone: Mapped[str | None]  # телефон
    profname: Mapped[str | None] # отображаемое имя профиля
    first_name: Mapped[str | None] # имя
    last_name: Mapped[str | None] # фамилия
    bio: Mapped[str | None] # о себе
    register_at: Mapped[str | None] # дата и время регистрации
    profile_visibility: Mapped[str | None] # видимость профиля (public, friends, private)
    message_privacy: Mapped[str | None] # кто может отправлять сообщения (everyone, friends, no_one)
    post_visibility: Mapped[str | None] # видимость постов (public, friends, private)



engine = create_async_engine(url)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def create_db_and_tables():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)