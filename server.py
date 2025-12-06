from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sensecache.api.router import router as api_router
from sensecache.api.errors import sense_cache_exception_handler
from sensecache.core.config import settings
from sensecache.core.exceptions import SenseCacheError
from sensecache.core.logger import configure_logger, get_logger
from sensecache.core.http_client import HttpClientManager

# Configure logging early
configure_logger(settings.LOG_LEVEL)
logger = get_logger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Lifespan context manager for FastAPI application.
    Handles startup and shutdown events.
    """
    logger.info("Starting Sense Cache", env=settings.model_dump())
    
    # Startup logic here (e.g., connect to DB, warm up cache)
    await HttpClientManager.start()
    
    yield
    
    # Shutdown logic here (e.g., close connections)
    await HttpClientManager.stop()
    logger.info("Shutting down Sense Cache")

def create_app() -> FastAPI:
    """
    Factory function to create the FastAPI application.
    """
    app = FastAPI(
        title="Sense Cache",
        description="Production-grade semantic caching proxy for LLM APIs",
        version="0.1.0",
        lifespan=lifespan,
    )

    # Middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Configure appropriately for production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Exception Handlers
    app.add_exception_handler(SenseCacheError, sense_cache_exception_handler)

    # Routers
    app.include_router(api_router, prefix="/v1")

    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
