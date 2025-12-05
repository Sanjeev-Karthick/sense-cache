from typing import Protocol, List, Dict, Optional, Any

class BaseCache(Protocol):
    """
    Protocol defining the interface for cache backends.
    """
    async def get(self, key: str) -> Dict[str, Any] | None:
        """
        Retrieve a value from the cache.
        
        Args:
            key: The cache key.
            
        Returns:
            The cached value as a dictionary, or None if not found.
        """
        ...

    async def set(self, key: str, value: Dict[str, Any], ttl: int) -> None:
        """
        Set a value in the cache.
        
        Args:
            key: The cache key.
            value: The value to cache (must be serializable to dict).
            ttl: Time to live in seconds.
        """
        ...

    async def search(self, embedding: List[float], namespace: str) -> List[Dict[str, Any]]:
        """
        Search for similar items in the cache using vector similarity.
        
        Args:
            embedding: The query embedding vector.
            namespace: The namespace to search in.
            
        Returns:
            A list of similar items found in the cache.
        """
        ...
