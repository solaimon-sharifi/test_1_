"""Trigonometric functions for the calculator."""
import math


def sin(angle_radians):
    """Return the sine of angle_radians.

    The input is interpreted in radians.
    """
    return math.sin(angle_radians)


def cos(angle_radians):
    """Return the cosine of angle_radians.

    The input is interpreted in radians.
    """
    return math.cos(angle_radians)


def tan(angle_radians):
    """Return the tangent of angle_radians.

    Raises ValueError when the cosine is (close to) zero because tangent
    would be undefined.
    """
    if abs(math.cos(angle_radians)) < 1e-12:
        raise ValueError("Tangent is undefined at this value")
    return math.tan(angle_radians)
