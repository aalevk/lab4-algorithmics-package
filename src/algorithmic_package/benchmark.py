from statistics import median
from time import perf_counter

from algorithmic_package.bubble import bubble_sort
from algorithmic_package.generators import generate_almost_sorted, generate_sorted
from algorithmic_package.merge import merge_sort


def measure(sort_function, original):
    times = []
    for _ in range(5):
        spisok = original.copy()
        start = perf_counter()
        sort_function(spisok)
        finish = perf_counter() - start
        times.append(finish)
    return median(times), times

def benchmark_sorted():
    sizes = (100_000, 1_000_000, 10_000_000)

    for size in sizes:
        original = generate_sorted(size)
        bubble_time, _ = measure(bubble_sort, original)
        merge_time, _ = measure(merge_sort, original)

        print(f"| Отсортированный | {size} | {bubble_time:.6f} | {merge_time:.6f} |")


def almost_sorted(seed = 52):
    sizes = (100_000, 1_000_000, 10_000_000)

    for size in sizes:
        original = generate_almost_sorted(size, seed = seed)
        bubble_time, _ = measure(bubble_sort, original)
        merge_time, _ = measure(merge_sort, original)

        print(
            f"| Почти отсортированный | {size} | {bubble_time:.6f} | {merge_time:.6f} |"
        )

if __name__ == "__main__":
    print("| Тип входа | Размер | Bubble Sort, с | Merge Sort, с |")
    print("|---|---:|---:|---:|")
    benchmark_sorted()
    almost_sorted()
