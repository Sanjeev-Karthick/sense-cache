import logging
import sys
from typing import Any

import structlog

def configure_logger(log_level: str = "INFO") -> None:
    """
    Configures structlog for production use.
    
    Args:
        log_level: The logging level to use (e.g., "INFO", "DEBUG").
    """
    shared_processors: list[Any] = [
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
    ]

    structlog.configure(
        processors=shared_processors + [
            structlog.processors.JSONRenderer(),
        ],
        logger_factory=structlog.PrintLoggerFactory(),
        wrapper_class=structlog.make_filtering_bound_logger(logging.getLevelName(log_level)),
        cache_logger_on_first_use=True,
    )

    # Configure standard library logging to use structlog
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=logging.getLevelName(log_level),
    )

def get_logger(name: str) -> structlog.stdlib.BoundLogger:
    """
    Returns a structured logger instance.
    
    Args:
        name: The name of the logger.
        
    Returns:
        A structlog bound logger.
    """
    return structlog.get_logger(name)
