import random

from algorithmic_package.generators import (
    generate_almost_sorted,
    generate_back_sorted,
    generate_duplicates_random,
    generate_random,
    generate_sorted,
)


def test_random_list():
    numbers = generate_random(10, seed=52)

    assert len(numbers) == 10
    assert all(type(number) is int for number in numbers)


def test_same_seed():
    assert generate_random(100, seed=52) == generate_random(100, seed=52)
    assert generate_duplicates_random(100, seed=52) == generate_duplicates_random(
        100, seed=52
    )
    assert generate_almost_sorted(100, seed=52) == generate_almost_sorted(100, seed=52)


def test_different_seeds():
    for generate in (generate_random, generate_duplicates_random):
        assert generate(100, seed=1) != generate(100, seed=2)


def test_sorted_and_reversed():
    assert generate_sorted(4) == [1, 2, 3, 4]
    assert generate_back_sorted(4) == [4, 3, 2, 1]


def test_duplicates():
    numbers = generate_duplicates_random(100, seed=52)

    assert len(numbers) == 100
    assert len(set(numbers)) <= 21


def test_almost_sorted():
    original = generate_sorted(100)
    numbers = generate_almost_sorted(100, seed=52)

    assert numbers != original
    assert sorted(numbers) == original
    for index in range(len(numbers)):
        assert abs(numbers[index] - original[index]) <= 1


def test_empty_lists():
    assert generate_sorted(0) == []
    assert generate_back_sorted(0) == []
    assert generate_random(0, seed=52) == []
    assert generate_duplicates_random(0, seed=52) == []
    assert generate_almost_sorted(0, seed=52) == []


def test_random_state():
    state = random.getstate()

    generate_random(10, seed=52)
    generate_duplicates_random(10, seed=52)
    generate_almost_sorted(10, seed=52)

    assert random.getstate() == state
