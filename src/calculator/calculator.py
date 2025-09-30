"""Calculator implementation that uses our operations."""
from .operations import add, subtract, multiply, divide

class Calculator:
    """Calculator class to perform arithmetic operations."""
    
    def __init__(self):
        """Initialize calculator with memory set to 0."""
        self.memory = 0
    
    def add(self, a, b):
        """Add two numbers."""
        return add(a, b)
    
    def subtract(self, a, b):
        """Subtract b from a."""
        return subtract(a, b)
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        return multiply(a, b)
    
    def divide(self, a, b):
        """Divide a by b."""
        return divide(a, b)
    
    def memory_store(self, value):
        """Store a value in memory."""
        self.memory = value
    
    def memory_recall(self):
        """Recall the value from memory."""
        return self.memory
    
    def memory_clear(self):
        """Clear the memory."""
        self.memory = 0

        # Add to imports in calculator.py
from .scientific import square_root, power

# Add these methods to the Calculator class
def square_root(self, x):
    """Calculate the square root of x."""
    return square_root(x)

def power(self, base, exponent):
    """Calculate base raised to the power of exponent."""
    return power(base, exponent)

    def memory_add(self, value):
    """
    Add a value to the memory.
    
    Args:
        value: Value to add to memory
    """
    self.memory += value

def memory_subtract(self, value):
    """
    Subtract a value from the memory.
    
    Args:
        value: Value to subtract from memory
    """
    self.memory -= value
    