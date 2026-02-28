import pytest
from calculator import (
    Calculator,
    DivisionByZeroError,
    InvalidInputError
)

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (2.5, 0.5, 3.0),
        (0, 0, 0),
    ],
)
def test_add(a, b, expected):
    assert Calculator.add(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),
        (0, 5, -5),
        (-3, -3, 0),
        (2.5, 1.5, 1.0),
    ],
)
def test_subtract(a, b, expected):
    assert Calculator.subtract(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (5, 0, 0),
        (-2, 3, -6),
        (2.5, 2, 5.0),
    ],
)
def test_multiply(a, b, expected):
    assert Calculator.multiply(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2),
        (5, 2, 2.5),
        (-10, 2, -5),
        (2.5, 0.5, 5.0),
    ],
)
def test_divide_valid(a, b, expected):
    assert Calculator.divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(DivisionByZeroError):
        Calculator.divide(10, 0)

@pytest.mark.parametrize(
    "base, exponent, expected",
    [
        (2, 3, 8),
        (5, 0, 1),
        (4, 0.5, 2),
        (2, -1, 0.5),
    ],
)
def test_power(base, exponent, expected):
    assert Calculator.power(base, exponent) == expected

@pytest.mark.parametrize(
    "value, expected",
    [
        (4, 2),
        (9, 3),
        (2.25, 1.5),
        (0, 0),
    ],
)
def test_sqrt_valid(value, expected):
    assert Calculator.sqrt(value) == expected


def test_sqrt_negative():
    with pytest.raises(InvalidInputError):
        Calculator.sqrt(-1)

@pytest.mark.parametrize(
    "value, expected",
    [
        (0, 1),
        (1, 1),
        (5, 120),
        (7, 5040),
    ],
)
def test_factorial_valid(value, expected):
    assert Calculator.factorial(value) == expected


@pytest.mark.parametrize("value", [-1, 2.5, "string"])
def test_factorial_invalid(value):
    with pytest.raises(InvalidInputError):
        Calculator.factorial(value)


@pytest.mark.parametrize(
    "value, expected",
    [
        (2, True),
        (3, True),
        (4, False),
        (17, True),
        (18, False),
        (1, False),
        (0, False),
        (-5, False),
    ],
)
def test_is_prime_number(value, expected):
    assert Calculator.is_prime_number(value) == expected


def test_is_prime_invalid_type():
    with pytest.raises(InvalidInputError):
        Calculator.is_prime_number(2.5)