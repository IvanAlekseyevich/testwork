
# from pydantic_settings import BaseSettings, SettingsConfigDict

from environs import Env

env = Env()
env.read_env()


DATABASE_URL = env.str("DATABASE_URL")
ALLOWED_HOST: str = "localhost"
app_title: str = "Благотворительный фонд QRKot"
app_description: str = "Сервис для поддержки нуждающихся"

# from pydantic import BaseModel


# class Settings(BaseModel):
#     app_title: str = "Благотворительный фонд QRKot"
#     app_description: str = "Сервис для поддержки нуждающихся"
#     database_url: str = "sqlite+aiosqlite:///fastapi.db"
#     hash_gen_key: str = "Secret"
#
#     class Config:
#         env_file = ".env"
#
#
# settings = Settings()
# class Settings(BaseSettings):
#     DB_HOST: str = "localhost"
#     DB_PORT: str = "5432"
#     DB_NAME: str = "db"
#     DB_USER: str = "root"
#     DB_PASS: str = "root"
#
#     SECRET_KEY: str = "your_secret_key"
#
#     model_config = SettingsConfigDict(case_sensitive=True)
#
#     @property
#     def database_url(self) -> str:
#         return (
#             "postgresql+asyncpg://"
#             f"{self.DB_USER}:{self.DB_PASS}"
#             f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
#         )


# settings = Settings()
