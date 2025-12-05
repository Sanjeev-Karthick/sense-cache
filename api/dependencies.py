from typing import AsyncGenerator
from sensecache.cache.base import BaseCache
from sensecache.cache.redis_cache import RedisCache
from sensecache.cache.memory_cache import MemoryCache
from sensecache.core.config import settings
from sensecache.embeddings.embedder import Embedder

# Global instances for reuse
_cache_backend: BaseCache | None = None
_embedder: Embedder | None = None

async def get_cache_backend() -> AsyncGenerator[BaseCache, None]:
    """
    Dependency to get the configured cache backend.
    """
    global _cache_backend
    if _cache_backend is None:
        if settings.CACHE_BACKEND == "redis":
            _cache_backend = RedisCache()
        else:
            _cache_backend = MemoryCache()
    
    yield _cache_backend

def get_embedder() -> Embedder:
    """
    Dependency to get the embedder instance.
    """
    global _embedder
    if _embedder is None:
        _embedder = Embedder()
    return _embedder
