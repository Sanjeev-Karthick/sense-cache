import httpx
from typing import Dict, Any, Optional
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

from sensecache.core.config import settings
from sensecache.core.logger import get_logger
from sensecache.core.exceptions import SenseCacheError
from sensecache.core.http_client import HttpClientManager
from sensecache.services.llm_interface import LLMClient
from sensecache.models.openai.chat_request import ChatCompletionRequest

logger = get_logger(__name__)

class OpenAIClient(LLMClient):
    """
    Production-grade client for interacting with OpenAI API.
    Features:
    - Connection Pooling (via HttpClientManager)
    - Automatic Retries (via Tenacity)
    - Type Safety (via Pydantic models)
    """
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or settings.OPENAI_API_KEY
        self.base_url = "https://api.openai.com/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    @retry(
        retry=retry_if_exception_type((httpx.RequestError, httpx.TimeoutException)),
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        reraise=True
    )
    async def chat_completions(self, request: ChatCompletionRequest) -> Dict[str, Any]:
        """
        Send a chat completion request to OpenAI with retries.
        """
        url = f"{self.base_url}/chat/completions"
        
        # Access the global singleton client
        client = HttpClientManager.get_client()
        
        # Pydantic dump
        payload = request.model_dump(exclude_none=True)
        
        logger.info("Forwarding request to OpenAI", model=payload.get("model"))
        
        try:
            response = await client.post(
                url, 
                headers=self.headers, 
                json=payload
            )
            
            if response.status_code != 200:
                logger.error(
                    "Upstream OpenAI error", 
                    status_code=response.status_code, 
                    details=response.text
                )
                # Parse error safely
                try:
                    error_data = response.json()
                    error_msg = error_data.get("error", {}).get("message", response.text)
                except Exception:
                    error_msg = response.text
                    
                raise SenseCacheError(f"OpenAI API Error: {error_msg}")
            
            return response.json()
            
        except httpx.RequestError as e:
            logger.warning(f"Network error (attempting retry if eligible): {str(e)}")
            raise e  # Allow tenacity to catch and retry
        except Exception as e:
            if isinstance(e, SenseCacheError):
                raise e
            logger.error("Unexpected error in OpenAI Client", error=str(e))
            raise SenseCacheError(f"Internal proxy error: {str(e)}")
