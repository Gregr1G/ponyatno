from fastapi import APIRouter
from src.Info.endpoints import router_info
from src.Tape.endpoints import router as router_tape
from src.Auth.schemas import UserRead, UserCreate, UserUpdate
from src.Auth.users import auth_backend
from src.Auth.manager import fastapi_users
def get_apps_router():
    router = APIRouter()

    router.include_router(router_info)
    router.include_router(router_tape)
    router.include_router(
        fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
    )

    router.include_router(
        fastapi_users.get_register_router(UserRead, UserCreate),
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