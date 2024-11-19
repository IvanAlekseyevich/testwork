from environs import Env
from pydantic_settings import BaseSettings

env = Env()
env.read_env()


class Settings(BaseSettings):
    APP_TITTLE: str = "Тестовое задание"
    APP_DESCRIPTION: str = "Сервис для расчета стоимости страховки товаров"
    DATABASE_URL = env.str("DATABASE_URL")

    ALLOWED_HOST: str = "localhost"
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    DB_NAME: str = "db"
    DB_USER: str = "root"
    DB_PASS: str = "root"
    SECRET_KEY: str = "your_secret_key"

    class Config:
        env_file = ".env"

    # @property
    # def database_url(self) -> str:
    #     return (
    #         "postgresql+asyncpg://"
    #         f"{self.DB_USER}:{self.DB_PASS}"
    #         f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    #     )


settings = Settings()
