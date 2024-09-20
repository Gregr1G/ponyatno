from sqlalchemy import select
from database import async_session_maker as async_session
from src.Auth.invates.models import Invite
from src.Auth.invates.services import generate_code
# import asyncio


class InviteRepository:
    @classmethod
    async def get_free_invite(cls, invite_code: str):
        async with async_session() as session:
            result = await session.execute(select(Invite).where(Invite.user_id == None).where(Invite.code == invite_code))
            # print(result.scalars().all()[0].__dict__)
        return result.scalars().all()

    @classmethod
    async def generate_invite(cls, inviter_id, admin_status=False):
        text = generate_code()

        async with async_session() as session:
            session.add(Invite(code=text, admin_status=admin_status, inviter_id=inviter_id))
            await session.commit()

        return text

    @classmethod
    async def get_users_invites(cls, inviter):
        async with async_session() as session:
            result = await session.execute(select(Invite).where(Invite.inviter_id == inviter))
        return result.scalars().all()

    @classmethod
    async def update_invites_user_id(cls, invite_code, user_id):
        async with async_session() as session:
            invite = await session.execute(select(Invite).where(Invite.code == invite_code))
            result = invite.scalars().first()

            if (not result.admin_status) and (result.user_id == None):
                result.user_id = user_id

            await session.commit()

# asyncio.run(InviteRepository.get_invite("kkGXuGujYsNfuEfpQ2WqZMySx"))