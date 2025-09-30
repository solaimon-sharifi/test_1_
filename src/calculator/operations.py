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
    """Multiply two numbers and return the product."""
    return left * right


def divide(left, right):
    """Divide left by right and return the quotient.

    Raises:
        ZeroDivisionError: If right is zero.
    """
    if right == 0:
        raise ZeroDivisionError("division by zero")
    return left / right
