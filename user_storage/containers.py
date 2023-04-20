from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import (
    Configuration,
    Resource
)
from pydantic import BaseSettings
from user_storage.adapter.db_adapter import UserDB


def init(clinet_type):
    async def w(*args, **kwargs):
        clinet = clinet_type(*args, **kwargs)
        await clinet.startup()
        yield clinet
        await clinet.shutdown()
    return w


class Container(DeclarativeContainer):
    config: Configuration = Configuration()

    # DB_DSN: str = f"postgresql://{config.DB_USER.required()}:{config.DB_PASS.required()}" \
    #               f"@{config.DB_HOST.required()}:{config.DB_PORT.required()}/{config.DB.required()}"
    db: Resource[UserDB] = Resource(
        init(UserDB),
        db_user=config.DB_USER.required(),
        db_pass=config.DB_PASS.required(),
        db_host=config.DB_HOST.required(),
        db_port=config.DB_PORT.required(),
        db=config.DB.required(),
    )

    @classmethod
    def create_container(cls, settings: BaseSettings) -> 'Container':
        container: cls = cls()
        container.config.from_pydantic(settings)
        return container
