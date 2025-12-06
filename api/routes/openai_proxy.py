from fastapi import APIRouter, HTTPException, BackgroundTasks, Depends
from sensecache.models.openai.chat_request import ChatCompletionRequest
from sensecache.models.openai.chat_response import ChatCompletionResponse
from sensecache.services.llm_interface import LLMClient
from sensecache.api.dependencies import get_llm_client
from sensecache.core.logger import get_logger
from sensecache.core.exceptions import SenseCacheError

router = APIRouter()
logger = get_logger(__name__)

@router.post("/chat/completions", response_model=ChatCompletionResponse)
async def chat_completions(
    request: ChatCompletionRequest,
    client: LLMClient = Depends(get_llm_client)
):
    """
    Proxy request to OpenAI Chat Completions API.
    
    Future:
    - Day 3: Intercept for semantic caching.
    - Day 4: Auth middleware / Rate limiting.
    - Day 5: Streaming support.
    """
    logger.info("Received chat completion request", model=request.model)
    
    try:
        # Call upstream OpenAI
        response_data = await client.chat_completions(request)
        
        # Validate/Parse response
        response = ChatCompletionResponse(**response_data)
        
        return response
        
    except SenseCacheError as e:
        logger.error("Sense Cache Error", error=str(e))
        # Convert internal exception to correct HTTP status
        # For now, 502 Bad Gateway is appropriate for upstream failures
        raise HTTPException(status_code=502, detail=str(e))
    except Exception as e:
        logger.error("Unhandled Exception", error=str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")
