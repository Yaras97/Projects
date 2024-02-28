def range_sum(numbers, start, end):
    # Базовый случай: если start больше end, возвращаем 0
    if start > end:
        return 0

    # Рекурсивный случай: суммируем текущий элемент и результат рекурсивного вызова для оставшейся части списка
    return numbers[start] + range_sum(numbers, start + 1, end)


print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))
