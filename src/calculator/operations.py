"""Basic arithmetic operations for the calculator.

This module provides elementary math functions for the calculator.
"""
from .logging_config import get_logger

logger = get_logger(__name__)


def add(left, right):
    """Add two numbers and return the result."""
    result = left + right
    logger.debug("add: %s + %s = %s", left, right, result)
    return result


def subtract(left, right):
    """Subtract right from left and return the result."""
    result = left - right
    logger.debug("subtract: %s - %s = %s", left, right, result)
    return result


def multiply(left, right):
    """Multiply two numbers and return the result."""
    result = left * right
    logger.debug("multiply: %s * %s = %s", left, right, result)
    return result


def divide(left, right):
    """
    Divide a by b and return the result.
    
    Args:
        a: The dividend
        b: The divisor
            
    Returns:
        The quotient a/b
            
    Raises:
        ZeroDivisionError: If b is 0
    """
    if right == 0:
        logger.error("divide: attempted division by zero: %s / %s", left, right)
        raise ZeroDivisionError("Cannot divide by zero")
    result = left / right
    logger.debug("divide: %s / %s = %s", left, right, result)
    return result
