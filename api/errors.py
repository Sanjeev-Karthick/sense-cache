from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from sensecache.core.exceptions import SenseCacheError

async def sense_cache_exception_handler(request: Request, exc: SenseCacheError) -> JSONResponse:
    """
    Global exception handler for SenseCacheError.
    """
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc), "type": exc.__class__.__name__},
    )

class ServiceUnavailable(HTTPException):
    def __init__(self, detail: str = "Service unavailable"):
        super().__init__(status_code=503, detail=detail)
