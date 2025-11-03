"""Simple logging configuration for the calculator package.

Provides a get_logger(name) helper so modules can obtain a module-scoped
logger with a consistent format.
"""
import logging


def get_logger(name: str) -> logging.Logger:
    """Return a configured logger for the given module name.

    This function is idempotent: calling repeatedly will not add duplicate
    handlers.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    # Default to INFO to avoid noisy debug logs in CI unless explicitly set
    logger.setLevel(logging.INFO)
    return logger
