from fastapi import APIRouter, Depends
from user_storage.containers import Container
from dependency_injector.wiring import Provide, inject
from user_storage.adapter.db_adapter import UserDB

checker_router: APIRouter = APIRouter()


@checker_router.get("/health", status_code=200)
async def health_check() -> None:
    """health check"""
    return None


@checker_router.get("/readiness", status_code=200)
@inject
async def readiness_check(
    db: UserDB = Depends(Provide[Container.db])
) -> None:
    """readiness check"""
    await db.check()
    return None
