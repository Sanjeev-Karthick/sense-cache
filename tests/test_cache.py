import pytest
from sensecache.cache.memory_cache import MemoryCache

@pytest.mark.asyncio
async def test_memory_cache_set_get():
    cache = MemoryCache()
    await cache.set("test_key", {"foo": "bar"}, ttl=60)
    
    result = await cache.get("test_key")
    assert result == {"foo": "bar"}

@pytest.mark.asyncio
async def test_memory_cache_miss():
    cache = MemoryCache()
    result = await cache.get("non_existent")
    assert result is None
