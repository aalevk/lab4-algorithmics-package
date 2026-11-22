from algorithmic_package.exceptions import (
    DeepRecursionError,
    NegativeNumberError,
    NotAnInteger,
)


def recursion_ladder(n):
    if type(n) is not int:
        raise NotAnInteger("Число ступеней должно быть целым")
    if n < 0:
        raise NegativeNumberError("Отрицательное число")
    if n > 30:
        raise DeepRecursionError("Слишком большое число для рекурсии")
    if n in [0, 1]:
        return 1
    else:
        return recursion_ladder(n-1) + recursion_ladder(n-2)


def iteration_ladder(n):
    if type(n) is not int:
        raise NotAnInteger("Число ступеней должно быть целым")
    if n < 0:
        raise NegativeNumberError("Отрицательное число")
    if n in [0, 1]:
        return 1
    a = 1
    b = 1
    for step in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b
