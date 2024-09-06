from typing import Type
from src.Auth.schemas import InviteCode
from fastapi import APIRouter, Depends, HTTPException, Request, status
from src.Auth.invates.models import *

from fastapi_users import exceptions, models, schemas
from fastapi_users.manager import BaseUserManager, UserManagerDependency
from fastapi_users.router.common import ErrorCode, ErrorModel
from src.Auth.repositories.invites_repository import InviteRepository


def get_register_router(
    get_user_manager: UserManagerDependency[models.UP, models.ID],
    user_schema: Type[schemas.U],
    user_create_schema: Type[schemas.UC],
    invite_schema: Type[InviteCode]
) -> APIRouter:
    """Generate a router with the register route."""
    router = APIRouter()

    @router.post(
        "/register",
        response_model=None,
        status_code=status.HTTP_201_CREATED,
        name="register:register",
        responses={
            status.HTTP_400_BAD_REQUEST: {
                "model": ErrorModel,
                "content": {
                    "application/json": {
                        "examples": {
                            ErrorCode.REGISTER_USER_ALREADY_EXISTS: {
                                "summary": "A user with this email already exists.",
                                "value": {
                                    "detail": ErrorCode.REGISTER_USER_ALREADY_EXISTS
                                },
                            },
                            ErrorCode.REGISTER_INVALID_PASSWORD: {
                                "summary": "Password validation failed.",
                                "value": {
                                    "detail": {
                                        "code": ErrorCode.REGISTER_INVALID_PASSWORD,
                                        "reason": "Password should be"
                                        "at least 3 characters",
                                    }
                                },
                            },
                        }
                    }
                },
            },
        },
    )
    async def register(
        request: Request,
        user_create: user_create_schema,
        invite_code: invite_schema,
        user_manager: BaseUserManager[models.UP, models.ID] = Depends(get_user_manager),
    ) -> user_schema | dict:

        try:
            code = await InviteRepository.get_free_invite(invite_code.code)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid invite code")

        if code:
            try:
                created_user = await user_manager.create(
                    user_create, safe=True, request=request
                )
            except exceptions.UserAlreadyExists:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=ErrorCode.REGISTER_USER_ALREADY_EXISTS,
                )
            except exceptions.InvalidPasswordException as e:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail={
                        "code": ErrorCode.REGISTER_INVALID_PASSWORD,
                        "reason": e.reason,
                    },
                )

            await InviteRepository.update_invites_user_id(invite_code.code, created_user.id)

            return schemas.model_validate(user_schema, created_user)
        else:
            return {"status": "error"}
    return router