from typing import List, Optional, Dict, Any, Literal
from pydantic import BaseModel

class ChatChoice(BaseModel):
    """
    A single completion choice.
    """
    index: int
    message: Dict[str, Any]
    finish_reason: Optional[str] = None

class Usage(BaseModel):
    """
    Token usage statistics.
    """
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int

class ChatCompletionResponse(BaseModel):
    """
    Response model for OpenAI Chat Completions API.
    """
    id: str
    object: str = "chat.completion"
    created: int
    model: str
    choices: List[ChatChoice]
    usage: Optional[Usage] = None
    system_fingerprint: Optional[str] = None
