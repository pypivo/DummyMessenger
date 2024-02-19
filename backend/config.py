from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    server_host: str = "0.0.0.0"
    server_port: int = 8080
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB_NAME: str = "postgres"
    POSTGRES_PORT: int = 5432
    DATABASE_URL: str = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_DB_NAME}:{POSTGRES_PORT}/{POSTGRES_DB_NAME}"
    # DATABASE_URL: str = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{server_host}:{POSTGRES_PORT}/{POSTGRES_DB_NAME}"


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)