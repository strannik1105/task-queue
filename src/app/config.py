from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000
