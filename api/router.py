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

from sensecache.api.routes import openai_proxy
router.include_router(openai_proxy.router, tags=["OpenAI"])
