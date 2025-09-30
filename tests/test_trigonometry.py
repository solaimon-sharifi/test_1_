"""Tests for the trigonometry helper functions."""
import math
import pytest

from calculator import trigonometry as trig


def test_sin_cos_basic():
    assert pytest.approx(trig.sin(0.0), rel=1e-9) == 0.0
    assert pytest.approx(trig.cos(0.0), rel=1e-9) == 1.0


def test_sin_pi_over_two():
    assert pytest.approx(trig.sin(math.pi / 2), rel=1e-9) == 1.0


def test_tan_basic():
    assert pytest.approx(trig.tan(0.0), rel=1e-9) == 0.0


def test_tan_undefined():
    # tangent is undefined at pi/2
    with pytest.raises(ValueError):
        trig.tan(math.pi / 2)
