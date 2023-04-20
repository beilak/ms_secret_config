from pydantic import BaseSettings


class Settings(BaseSettings):

    DB_USER: str
    DB_PASS: str
    DB: str
    DB_HOST: str
    DB_PORT: int
