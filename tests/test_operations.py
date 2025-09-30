"""Tests for calculator operations."""

from calculator.operations import add, subtract

def test_add():
    """Test the add function."""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    """Test the subtract function."""
    assert subtract(3, 2) == 1
    assert subtract(2, 3) == -1
    assert subtract(0, 0) == 0