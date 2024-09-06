from fastapi import APIRouter, Depends
from src.Auth.repositories.invites_repository import InviteRepository

from database import User
from src.Auth.manager import current_user

invite_router = APIRouter()


@invite_router.post("/generate")
async def generate_invite(user: User = Depends(current_user)):
    await InviteRepository.generate_invite(user.id, user.is_superuser)
    unused_invites = [i.code for i in await InviteRepository.get_users_invites(user.id)]

    return {"codes": unused_invites,
            "count": f"{len(unused_invites)}/9"}


# @invite_router.get("/get_invites")
# async def get_invites_count():
#     pass