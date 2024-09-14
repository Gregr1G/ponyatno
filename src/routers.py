from fastapi import APIRouter
from src.Info.endpoints import router_info
from src.Post.endpoints import post_router
from src.Auth.schemas import UserRead, UserCreate, UserUpdate, InviteCode
from src.Auth.users import auth_backend
from src.Auth.manager import fastapi_users, get_user_manager
from src.Auth.register import get_register_router
from src.Auth.invates.endpoints import invite_router


def get_apps_router():
    router = APIRouter()

    router.include_router(router_info)
    router.include_router(post_router)
    router.include_router(invite_router)
    router.include_router(
        fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
    )

    router.include_router(
        get_register_router(get_user_manager, UserRead, UserCreate, InviteCode),
        prefix="/auth",
        tags=["auth"],
    )
    router.include_router(
        fastapi_users.get_reset_password_router(),
        prefix="/auth",
        tags=["auth"],
    )
    router.include_router(
        fastapi_users.get_verify_router(UserRead),
        prefix="/auth",
        tags=["auth"],
    )
    router.include_router(
        fastapi_users.get_users_router(UserRead, UserUpdate),
        prefix="/users",
        tags=["users"],
    )

    return router