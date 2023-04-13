from fastapi import APIRouter

checker_router: APIRouter = APIRouter()


@checker_router.get("/health", status_code=200)
async def health_check() -> None:
    """health check"""
    return None


@checker_router.get("/readiness", status_code=200)
async def readiness_check() -> None:
    """readiness check"""
    return None
