from pydantic import BaseSettings


class Settings(BaseSettings):

    DB_DSN: str
    LOG_TEST: str
