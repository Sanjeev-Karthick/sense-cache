from typing import List, Dict, Any
from sensecache.core.exceptions import SenseCacheError

def validate_messages(messages: List[Dict[str, Any]]) -> None:
    """
    Validate that the messages list is not empty and follows basic structure.
    
    Args:
        messages: List of message dictionaries.
        
    Raises:
        SenseCacheError: If validation fails.
    """
    if not messages:
        raise SenseCacheError("Messages list cannot be empty.")
    
    # improved: check if the last message is from user (common requirement for chat completion in some contexts, 
    # though not strictly enforced by OpenAI API always, it's good practice for a cache proxy to maybe check this later)
    # For now, we just ensure it's not empty.
    pass
