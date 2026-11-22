from algorithmic_package.benchmark import measure
from algorithmic_package.bubble import bubble_sort


def test_measure():
    numbers = [3, 1, 2]

    _, times = measure(bubble_sort, numbers)

    assert len(times) == 5
    assert numbers == [3, 1, 2]
