"""
    Settings
"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """ Settings class """
    main_url: str  # export MAIN_URL=/
    env: str
    postgres_user: str
    postgres_password: str
    postgres_db: str


settings = Settings()
