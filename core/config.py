from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Application configuration loaded from environment variables.
    """
    OPENAI_API_KEY: str
    REDIS_URL: str = "redis://localhost:6379"
    CACHE_BACKEND: str = "redis"
    SIMILARITY_THRESHOLD: float = 0.85
    CACHE_TTL: int = 86400
    EMBED_MODEL: str = "text-embedding-3-small"
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

settings = Settings()
