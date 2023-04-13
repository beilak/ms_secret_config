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

    db: Resource[UserDB] = Resource(
        init(UserDB),
        dsn=config.DB_DSN.required()
    )

    @classmethod
    def create_container(cls, settings: BaseSettings) -> 'Container':
        container: cls = cls()
        container.config.from_pydantic(settings)
        return container
