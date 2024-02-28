from itertools import *


def first_largest(iterable, number):
    # Используем dropwhile, чтобы пропустить элементы, которые не больше number
    filtered_iterable = dropwhile(lambda x: x <= number, iterable)
    # filtered = len(list(takewhile(lambda x: x <= number, iterable)))
    # Используем islice и enumerate, чтобы получить индекс первого элемента, удовлетворяющего условию
    result = next(((index, value) for index, value in enumerate(filtered_iterable, start=0)), (-1, None))
    print(result[1])
    if result[1] != number:
        return filtered_iterable
    else:
        return result[0]


iterator = iter([18, 21, 14, 72, 73, 18, 20, 101, 102, 110])

print(first_largest(iterator, 105))


# def first_largest(iterable, number):
#     for index, element in enumerate(iterable):
#         if element > number:
#             return index
#     return -1