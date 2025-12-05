from typing import List, Dict, Any, Optional
from sensecache.cache.base import BaseCache
from sensecache.core.logger import get_logger

logger = get_logger(__name__)

class MemoryCache:
    """
    In-memory implementation of the BaseCache protocol.
    Useful for testing and development.
    """
    def __init__(self) -> None:
        self._store: Dict[str, Any] = {}
        logger.info("Initialized Memory cache")

    async def get(self, key: str) -> Dict[str, Any] | None:
        return self._store.get(key)

    async def set(self, key: str, value: Dict[str, Any], ttl: int) -> None:
        # Note: TTL is not implemented in this simple memory cache
        self._store[key] = value

    async def search(self, embedding: List[float], namespace: str) -> List[Dict[str, Any]]:
        # Placeholder for vector search implementation
        logger.warning("Memory vector search not implemented yet")
        return []
