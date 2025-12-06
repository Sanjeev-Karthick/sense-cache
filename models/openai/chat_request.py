from typing import List, Optional, Dict, Literal, Union, Any
from pydantic import BaseModel, Field, field_validator

class ChatMessage(BaseModel):
    """
    Represents a single message in the chat conversation.
    """
    role: Literal["system", "user", "assistant"]
    content: str
    name: Optional[str] = None

class ChatCompletionRequest(BaseModel):
    """
    Request model for OpenAI Chat Completions API.
    Ref: https://platform.openai.com/docs/api-reference/chat/create
    """
    model: str = Field(..., description="ID of the model to use.", examples=["gpt-3.5-turbo"])
    messages: List[ChatMessage] = Field(..., description="A list of messages comprising the conversation so far.")
    temperature: Optional[float] = Field(1.0, ge=0.0, le=2.0)
    top_p: Optional[float] = Field(1.0, ge=0.0, le=1.0)
    n: Optional[int] = Field(1, ge=1)
    stream: Optional[bool] = Field(False, description="If set, partial message deltas will be sent.")
    stop: Optional[Union[str, List[str]]] = None
    max_tokens: Optional[int] = None
    presence_penalty: Optional[float] = Field(0.0, ge=-2.0, le=2.0)
    frequency_penalty: Optional[float] = Field(0.0, ge=-2.0, le=2.0)
    logit_bias: Optional[Dict[str, float]] = None
    user: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": "Hello!"}
                ]
            }
        }
