from algorithmic_package.exceptions import InvalidDataTypeError, NotAnInteger


def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(spisok):
    if not isinstance(spisok, list):
        raise InvalidDataTypeError("Ожидается список")
    if not all(type(x) is int for x in spisok):
        raise NotAnInteger("Не все элементы списка - целые числа")
    if len(spisok) < 2:
        return spisok.copy()
    else:
        mid = len(spisok) // 2
        left = merge_sort(spisok[:mid])
        right = merge_sort(spisok[mid:])
        return merge(left, right)
