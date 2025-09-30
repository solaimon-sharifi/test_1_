"""Scientific calculator helper functions."""
import math


def square_root(value):
    """Return the square root of value.

    Raises ValueError for negative inputs.
    """
    if value < 0:
        raise ValueError("math domain error")
    return math.sqrt(value)


def power(base, exponent):
    """Return base raised to exponent."""
    return base ** exponent
