from typing import List
from sensecache.core.config import settings
from sensecache.core.logger import get_logger

logger = get_logger(__name__)

class Embedder:
    """
    Service for generating embeddings.
    """
    def __init__(self, model: str = settings.EMBED_MODEL):
        self.model = model
        logger.info("Initialized Embedder", model=model)

    async def embed(self, text: str) -> List[float]:
        """
        Generate embeddings for the given text.
        
        Args:
            text: The text to embed.
            
        Returns:
            A list of floats representing the embedding vector.
        """
        # Placeholder for OpenAI embedding call
        logger.info("Generating embedding", text_length=len(text))
        return [0.0] * 1536
