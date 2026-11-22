import pytest

from algorithmic_package.exceptions import (
    DeepRecursionError,
    NegativeNumberError,
    NotAnInteger,
)
from algorithmic_package.ladder import iteration_ladder, recursion_ladder


def test_small_ladder():
    for count in (recursion_ladder, iteration_ladder):
        assert count(0) == 1
        assert count(1) == 1
        assert count(2) == 2
        assert count(6) == 13


def test_negative_steps():
    for count in (recursion_ladder, iteration_ladder):
        with pytest.raises(NegativeNumberError):
            count(-1)


def test_wrong_type():
    for count in (recursion_ladder, iteration_ladder):
        with pytest.raises(NotAnInteger):
            count(-2.5)
        with pytest.raises(NotAnInteger):
            count("3")


def test_recursion_limit():
    with pytest.raises(DeepRecursionError):
        recursion_ladder(31)

    assert iteration_ladder(31) == 2178309
