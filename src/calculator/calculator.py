"""Calculator implementation that uses our operations and scientific helpers."""
from .operations import add as ops_add, subtract as ops_subtract, multiply as ops_multiply, divide as ops_divide
from .scientific import square_root as sci_sqrt, power as sci_power


class Calculator:
    """Calculator class to perform arithmetic operations and keep memory."""

    def __init__(self) -> None:
        """Initialize calculator with memory set to 0."""
        self.memory = 0

    # Basic operations (wrap the functions from operations.py)
    def add(self, a, b):
        return ops_add(a, b)

    def subtract(self, a, b):
        return ops_subtract(a, b)

    def multiply(self, a, b):
        return ops_multiply(a, b)

    def divide(self, a, b):
        return ops_divide(a, b)

    # Memory operations
    def memory_store(self, value):
        self.memory = value

    def memory_recall(self):
        return self.memory

    def memory_clear(self):
        self.memory = 0

    def memory_add(self, value):
        """Add a value to the stored memory."""
        self.memory += value

    def memory_subtract(self, value):
        """Subtract a value from the stored memory."""
        self.memory -= value

    # Scientific helpers delegate to scientific module
    def square_root(self, x):
        return sci_sqrt(x)

    def power(self, base, exponent):
        return sci_power(base, exponent)
