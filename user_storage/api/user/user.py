from fastapi import APIRouter, Depends, HTTPException
from dependency_injector.wiring import Provide, inject
import logging

from user_storage.models.user import User, UserResponse
from user_storage.containers import Container
from user_storage.adapter.db_adapter import UserDB

user_router: APIRouter = APIRouter()


@user_router.post(
    "/user",
    status_code=201,
    response_model=int,
    description="Create new user",
)
@inject
async def add_user(
        request: User,
        db: UserDB = Depends(Provide[Container.db])
) -> int:
    """Post new user"""
    logging.info(f" post new user { request = }")
    return await db.insert_user(request)


@user_router.get(
    "/user/{user_id}",
    status_code=200,
    response_model=UserResponse,
    description="Get user",
)
@inject
async def get_user(
        user_id: int,
        db: UserDB = Depends(Provide[Container.db])
) -> UserResponse:
    """Get user"""
    logging.info(f" read user { user_id = }")
    user = await db.read_user(user_id)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")


@user_router.delete(
    "/user/{user_id}",
    status_code=204,
    response_model=None,
    description="Del a user",
)
@inject
async def delete_user(
        user_id: int,
        db: UserDB = Depends(Provide[Container.db])
) -> None:
    """Delete user"""
    logging.info(f" Del user { user_id = }")
    await db.del_user(user_id)


@user_router.put(
    "/user/{user_id}",
    status_code=200,
    response_model=UserResponse,
    description="Change user",
)
@inject
async def upd_user(
        user_id: int,
        request: User,
        db: UserDB = Depends(Provide[Container.db])
) -> UserResponse:
    """Put user"""
    logging.info(f" put user { user_id = } with { request = }")
    await db.update_user(user_id, request)
    user = await db.read_user(user_id)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")
