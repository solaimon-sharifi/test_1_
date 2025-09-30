"""Calculator class implementation.

This module provides a Calculator class that uses the operations module.
"""
from .operations import add, subtract, multiply, divide


class Calculator:
    """A simple calculator class that provides basic arithmetic operations.

    This class uses the functions from the operations module to perform
    calculations and keeps track of calculation history.
    """

    def __init__(self):
        """Initialize a new Calculator with empty history."""
        self.history = []

    def add(self, a, b):
        result = add(a, b)
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = subtract(a, b)
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = multiply(a, b)
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        result = divide(a, b)
        self.history.append(f"{a} / {b} = {result}")
        return result

    def get_history(self):
        return self.history
