"""
Tests for the calculator module using pytest.
"""

import pytest
from calculator import add, subtract, multiply, divide


class TestAdd:
    """Tests for the add function."""

    def test_add_positive_numbers(self):
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        assert add(-2, -3) == -5

    def test_add_mixed_numbers(self):
        assert add(-2, 3) == 1

    def test_add_floats(self):
        assert add(2.5, 3.5) == 6.0

    def test_add_zero(self):
        assert add(5, 0) == 5


class TestSubtract:
    """Tests for the subtract function."""

    def test_subtract_positive_numbers(self):
        assert subtract(5, 3) == 2

    def test_subtract_negative_numbers(self):
        assert subtract(-5, -3) == -2

    def test_subtract_mixed_numbers(self):
        assert subtract(-2, 3) == -5

    def test_subtract_floats(self):
        assert subtract(5.5, 2.5) == 3.0

    def test_subtract_zero(self):
        assert subtract(5, 0) == 5


class TestMultiply:
    """Tests for the multiply function."""

    def test_multiply_positive_numbers(self):
        assert multiply(4, 3) == 12

    def test_multiply_negative_numbers(self):
        assert multiply(-4, -3) == 12

    def test_multiply_mixed_numbers(self):
        assert multiply(-4, 3) == -12

    def test_multiply_floats(self):
        assert multiply(2.5, 4) == 10.0

    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0


class TestDivide:
    """Tests for the divide function."""

    def test_divide_positive_numbers(self):
        assert divide(10, 2) == 5

    def test_divide_negative_numbers(self):
        assert divide(-10, -2) == 5

    def test_divide_mixed_numbers(self):
        assert divide(-10, 2) == -5

    def test_divide_floats(self):
        assert divide(7.5, 2.5) == 3.0

    def test_divide_by_zero_raises_error(self):
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            divide(10, 0)

    def test_divide_zero_by_number(self):
        assert divide(0, 5) == 0
