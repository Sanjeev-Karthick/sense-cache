class SenseCacheError(Exception):
    """Base exception for Sense Cache application."""
    pass

class ConfigurationError(SenseCacheError):
    """Raised when there is a configuration error."""
    pass

class CacheError(SenseCacheError):
    """Base exception for cache operations."""
    pass

class EmbeddingError(SenseCacheError):
    """Raised when embedding generation fails."""
    pass
