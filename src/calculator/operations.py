"""Basic arithmetic operations for the calculator.

This module provides elementary math functions for the calculator.
"""

def add(left, right):
    """Add two numbers and return the result."""
    return left + right


def subtract(left, right):
    """Subtract right from left and return the result."""
    return left - right


def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b

def divide(a, b):
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
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b