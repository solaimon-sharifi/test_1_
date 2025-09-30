"""Basic arithmetic operations for the calculator.

This module provides elementary math functions for the calculator.
"""

def add(left, right):
    """Add two numbers and return the result."""
    return left + right


def subtract(left, right):
    """Subtract right from left and return the result."""
    return left - right


def multiply(left, right):
    """Multiply two numbers and return the result."""
    return left * right


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
        raise ZeroDivisionError("Cannot divide by zero")
    return left / right
