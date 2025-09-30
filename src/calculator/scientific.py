"""Scientific calculator helper functions."""
import math


def square_root(x):
    """Return the square root of x.

    Raises ValueError for negative inputs.
    """
    if x < 0:
        raise ValueError("math domain error")
    return math.sqrt(x)


def power(base, exponent):
    """Return base raised to exponent."""
    return base ** exponent
