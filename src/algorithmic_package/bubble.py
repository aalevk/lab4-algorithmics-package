from algorithmic_package.exceptions import NotAnInteger, invalidDataTypeError


def bubble_sort(spisok):
    if not isinstance(spisok, list):
        raise invalidDataTypeError("Ожидается список")
    result = spisok.copy()
    if not all(type(x) is int for x in result):
        raise NotAnInteger("Не все элементы списка - целые числа")
    end = 0
    c = 1
    while c > 0:
        c = 0
        for i in range(len(result) - end - 1):
            if result[i] > result[i+1]:
                result[i], result[i+1] = result[i+1], result[i]
                c += 1
        end += 1
    return result