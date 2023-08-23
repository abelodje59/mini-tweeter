from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "mini-twitter"
    APP_VERSION: str = "0.0.1"
    SQLITE_URL: str = "sqlite://db.sqlite3"
    TORTOISE_MODELS: str = "models.twitter"
    JWT_SECRET: str ="please_please_update_me_please"
    JWT_ALGORITHM: str ="HS256"


settings = Settings()