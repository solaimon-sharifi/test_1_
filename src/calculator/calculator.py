"""Calculator implementation that uses our operations and scientific helpers."""
from .operations import (
    add as ops_add,
    subtract as ops_subtract,
    multiply as ops_multiply,
    divide as ops_divide,
)
from .scientific import (
    square_root as sci_sqrt,
    power as sci_power,
)


class Calculator:
    """Calculator class to perform arithmetic operations and keep memory.

    This class is a thin wrapper around the pure functions in
    :mod:`calculator.operations` and :mod:`calculator.scientific` so the
    public API is easier to test and extend.
    """

    def __init__(self) -> None:
        """Initialize calculator with memory set to 0."""
        self.memory = 0

    # Basic operations (wrap the functions from operations.py)
    def add(self, left, right):
        """Return left + right."""
        return ops_add(left, right)

    def subtract(self, left, right):
        """Return left - right."""
        return ops_subtract(left, right)

    def multiply(self, left, right):
        """Return left * right."""
        return ops_multiply(left, right)

    def divide(self, left, right):
        """Return left / right (raises ZeroDivisionError for div by 0)."""
        return ops_divide(left, right)

    # Memory operations
    def memory_store(self, value):
        """Store a numeric value in memory."""
        self.memory = value

    def memory_recall(self):
        """Return the stored memory value."""
        return self.memory

    def memory_clear(self):
        """Clear memory (set to 0)."""
        self.memory = 0

    def memory_add(self, value):
        """Add a value to the stored memory."""
        self.memory += value

    def memory_subtract(self, value):
        """Subtract a value from the stored memory."""
        self.memory -= value

    # Scientific helpers delegate to scientific module
    def square_root(self, value):
        """Return the square root of value (delegates to :func:`sci_sqrt`)."""
        return sci_sqrt(value)

    def power(self, base, exponent):
        """Return base ** exponent (delegates to :func:`sci_power`)."""
        return sci_power(base, exponent)
