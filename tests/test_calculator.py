"""Tests for the Calculator class."""
import pytest
from calculator.calculator import Calculator

@pytest.fixture
def calculator():
    """Create and return a Calculator instance for testing."""
    return Calculator()

def test_calculator_initialization(calculator):
    """Test that calculator initializes with memory set to 0."""
    assert calculator.memory_recall() == 0

def test_calculator_operations(calculator):
    """Test the basic calculator operations."""
    assert calculator.add(1, 2) == 3
    assert calculator.subtract(5, 3) == 2
    assert calculator.multiply(2, 4) == 8
    assert calculator.divide(10, 2) == 5

def test_memory_store_and_recall(calculator):
    """Test the memory store and recall functions."""
    calculator.memory_store(5)
    assert calculator.memory_recall() == 5

def test_memory_clear(calculator):
    """Test the memory clear function."""
    calculator.memory_store(5)
    calculator.memory_clear()
    assert calculator.memory_recall() == 0