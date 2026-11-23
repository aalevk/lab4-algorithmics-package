import pytest

from algorithmic_package.bubble import bubble_sort
from algorithmic_package.exceptions import InvalidDataTypeError, NotAnInteger
from algorithmic_package.generators import generate_random
from algorithmic_package.merge import merge_sort


def test_empty_list():
    assert bubble_sort([]) == []
    assert merge_sort([]) == []


def test_one_number():
    assert bubble_sort([7]) == [7]
    assert merge_sort([7]) == [7]


def test_sorted_list():
    numbers = [1, 2, 3]

    assert bubble_sort(numbers) == [1, 2, 3]
    assert merge_sort(numbers) == [1, 2, 3]


def test_reverse_list():
    numbers = [3, 2, 1]

    assert bubble_sort(numbers) == [1, 2, 3]
    assert merge_sort(numbers) == [1, 2, 3]


def test_negatives_and_duplicates():
    numbers = [3, -1, 3, 0]
    expected = [-1, 0, 3, 3]

    assert bubble_sort(numbers) == expected
    assert merge_sort(numbers) == expected


def test_random_list():
    numbers = generate_random(100, seed=52)
    expected = sorted(numbers)

    assert bubble_sort(numbers) == expected
    assert merge_sort(numbers) == expected


def test_original_list():
    for sort in (bubble_sort, merge_sort):
        numbers = [3, 1, 2]

        result = sort(numbers)

        assert result is not numbers
        assert numbers == [3, 1, 2]


def test_wrong_input():
    for sort in (bubble_sort, merge_sort):
        with pytest.raises(InvalidDataTypeError):
            sort((2, 1))


def test_wrong_element():
    for sort in (bubble_sort, merge_sort):
        with pytest.raises(NotAnInteger):
            sort([1.5])
