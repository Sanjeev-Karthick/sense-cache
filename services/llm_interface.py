from abc import ABC, abstractmethod
from typing import Dict, Any
from sensecache.models.openai.chat_request import ChatCompletionRequest

class LLMClient(ABC):
    """
    Abstract interface for LLM providers.
    Enforces a consistent contract for all model interactions.
    """
    
    @abstractmethod
    async def chat_completions(self, request: ChatCompletionRequest) -> Dict[str, Any]:
        """
        Send a chat completion request to the LLM provider.
        
        Args:
            request: The validated chat completion request.
            
        Returns:
            The raw JSON response from the provider (to be parsed by the caller).
        """
        pass
