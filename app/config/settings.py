from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "ReconX Engine"
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/reconx_db"
    REDIS_URL: str = "redis://localhost:6379"
    API_KEY: str = "test_api_key"

    model_config = SettingsConfigDict(
        env_file=".env.example",
        extra="ignore",
    )


settings = Settings()