from functools import lru_cache
from sensecache.services.llm_interface import LLMClient
from sensecache.services.openai_client import OpenAIClient

@lru_cache()
def get_llm_client() -> LLMClient:
    """
    Dependency injection provider for the LLM Client.
    Returns a singleton instance of the configured provider.
    """
    # In the future, we could switch implementations based on config here.
    return OpenAIClient()

from sensecache.cache.base import BaseCache
from sensecache.cache.redis_cache import RedisCache
from sensecache.core.config import settings

@lru_cache()
def get_cache_backend() -> BaseCache:
    """
    Dependency injection provider for the Cache Backend.
    """
    return RedisCache(settings.REDIS_URL)
