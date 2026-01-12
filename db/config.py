# app/config.py
from typing import ClassVar
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://postgres:Ghjuhtcc4410pos@db/dbtree"


settings = Settings()  # type: ignore
