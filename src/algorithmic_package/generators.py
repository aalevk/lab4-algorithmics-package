import random


def generate_random(n, seed):
    result = []
    start = random.Random(seed)
    for _ in range(n):
        result.append(start.randint(-1000, 1000))
    return result


def generate_duplicates_random(n, seed):
    result = []
    start = random.Random(seed)
    for _ in range(n):
        result.append(start.randint(-10, 10))
    return result


def generate_sorted(n):
    return ([x for x in range(1, n + 1)])


def generate_back_sorted(n):
    return ([n - x for x in range(n)])

def generate_almost_sorted(n, seed):
    result = generate_sorted(n)
    start = random.Random(seed)
    every = start.randint(4, 8)

    for i in range(every - 1, n - 1, every):
        result[i], result[i + 1] = result[i + 1], result[i]
    return result
