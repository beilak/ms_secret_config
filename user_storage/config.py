from pydantic import BaseSettings


class Settings(BaseSettings):

    DB_DSN: str = "postgresql://user_storage:user_storage@0.0.0.0:5432/user_storage"
