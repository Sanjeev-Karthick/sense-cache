import httpx
from typing import Optional
from sensecache.core.config import settings

class HttpClientManager:
    """
    Singleton manager for the global HTTP client.
    Ensures connection pooling and efficient resource usage.
    """
    _client: Optional[httpx.AsyncClient] = None

    @classmethod
    def get_client(cls) -> httpx.AsyncClient:
        """
        Get the global HTTP client instance.
        """
        if cls._client is None:
            # Lazy initialization if accessed before lifespan startup (fallback)
            # ideally lifespan should handle this.
            cls._client = cls._create_client()
        return cls._client

    @classmethod
    def _create_client(cls) -> httpx.AsyncClient:
        """
        Create a new AsyncClient with production-grade settings.
        """
        limits = httpx.Limits(max_keepalive_connections=50, max_connections=100)
        timeout = httpx.Timeout(60.0, connect=10.0)
        return httpx.AsyncClient(limits=limits, timeout=timeout)

    @classmethod
    async def start(cls) -> None:
        """Initialize the client."""
        if cls._client is None:
            cls._client = cls._create_client()

    @classmethod
    async def stop(cls) -> None:
        """Close the client."""
        if cls._client:
            await cls._client.aclose()
            cls._client = None
