"""Tests for scientific calculator operations."""
import pytest
import math
from calculator.scientific import square_root, power


def test_square_root():
    """Test the square root function."""
    assert square_root(4) == 2
    assert square_root(9) == 3
    assert square_root(2) == pytest.approx(1.414, 0.001)


def test_square_root_negative():
    """Test that square root of negative number raises ValueError."""
    with pytest.raises(ValueError):
        square_root(-1)


def test_power():
    """Test the power function."""
    assert power(2, 3) == 8
    assert power(5, 2) == 25
    assert power(4, 0.5) == 2