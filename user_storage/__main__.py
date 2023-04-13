from fastapi import FastAPI

from user_storage.api.probes.healthchecks import checker_router
from user_storage.api.user.user import user_router
from user_storage.config import Settings
from user_storage.containers import Container
from user_storage.api.user import user


async def startup() -> None:
    settings: Settings = Settings()
    container: Container = Container.create_container(settings)
    container.wire(
        modules=[user],
    )
    container.init_resources()
    setattr(API, "__container", container)


async def shutdown() -> None:
    getattr(API, "__container").shutdown_resources()


API: FastAPI = FastAPI(
    title="User Storage",
    description="User Storage",
    docs_url="/api/doc",
    on_startup=[startup],
    on_shutdown=[shutdown],
)

API.include_router(user_router, prefix="/api", tags=["user"])
API.include_router(checker_router, prefix="/check", tags=["Check"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(API, host="0.0.0.0", port=8081)
