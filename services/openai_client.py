import httpx
from typing import Dict, Any, Optional
from sensecache.core.config import settings
from sensecache.core.logger import get_logger
from sensecache.core.exceptions import SenseCacheError

logger = get_logger(__name__)

class OpenAIClient:
    """
    Client for interacting with OpenAI API.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or settings.OPENAI_API_KEY
        self.base_url = "https://api.openai.com/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    async def chat_completions(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Send a chat completion request to OpenAI.
        
        Args:
            payload: The request payload matching OpenAI's schema.
            
        Returns:
            The JSON response from OpenAI.
            
        Raises:
            SenseCacheError: If the upstream request fails.
        """
        url = f"{self.base_url}/chat/completions"
        
        logger.info("Forwarding request to OpenAI", model=payload.get("model"))
        
        async with httpx.AsyncClient(timeout=60.0) as client:
            try:
                response = await client.post(
                    url, 
                    headers=self.headers, 
                    json=payload
                )
                
                # Log latency if possible (httpx response object might have timing info, 
                # or we rely on the logger decorator/middleware for general latency)
                
                if response.status_code != 200:
                    logger.error(
                        "Upstream OpenAI error", 
                        status_code=response.status_code, 
                        details=response.text
                    )
                    # Attempt to parse OpenAI error
                    try:
                        error_data = response.json()
                        error_msg = error_data.get("error", {}).get("message", response.text)
                    except Exception:
                        error_msg = response.text
                        
                    raise SenseCacheError(f"OpenAI API Error: {error_msg}")
                
                return response.json()
                
            except httpx.RequestError as e:
                logger.error("Network error communicating with OpenAI", error=str(e))
                raise SenseCacheError(f"Network error: {str(e)}")
            except Exception as e:
                if isinstance(e, SenseCacheError):
                    raise e
                logger.error("Unexpected error in OpenAI Client", error=str(e))
                raise SenseCacheError(f"Internal proxy error: {str(e)}")
