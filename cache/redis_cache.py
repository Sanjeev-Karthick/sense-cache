import json
from typing import List, Dict, Any, Optional
import redis.asyncio as redis
from sensecache.cache.base import BaseCache
from sensecache.core.logger import get_logger
from sensecache.core.config import settings

logger = get_logger(__name__)

class RedisCache:
    """
    Redis implementation of the BaseCache protocol.
    """
    def __init__(self, url: str = settings.REDIS_URL):
        self.redis = redis.from_url(url, decode_responses=True)
        logger.info("Initialized Redis cache", url=url)

    async def get(self, key: str) -> Dict[str, Any] | None:
        try:
            value = await self.redis.get(key)
            if value:
                return json.loads(value)
            return None
        except Exception as e:
            logger.error("Error getting key from Redis", key=key, error=str(e))
            return None

    async def set(self, key: str, value: Dict[str, Any], ttl: int) -> None:
        try:
            await self.redis.set(key, json.dumps(value), ex=ttl)
        except Exception as e:
            logger.error("Error setting key in Redis", key=key, error=str(e))

    async def search(self, embedding: List[float], namespace: str) -> List[Dict[str, Any]]:
        # Placeholder for vector search implementation
        # In a real implementation, this would use Redis Stack's vector search capabilities
        logger.warning("Redis vector search not implemented yet")
        return []

    async def close(self) -> None:
        await self.redis.close()
