from fastapi import APIRouter, Depends
from sensecache.api.models import HealthResponse
from sensecache.api.dependencies import get_cache_backend
from sensecache.cache.base import BaseCache

router = APIRouter()

@router.get("/health", response_model=HealthResponse)
async def health_check(cache: BaseCache = Depends(get_cache_backend)) -> HealthResponse:
    """
    Health check endpoint.
    """
    return HealthResponse(status="ok")
