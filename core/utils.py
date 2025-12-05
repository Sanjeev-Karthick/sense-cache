import uuid

def generate_request_id() -> str:
    """
    Generates a unique request ID.
    
    Returns:
        A UUID4 string.
    """
    return str(uuid.uuid4())
