import time


def for_and_append():   # с использованием цикла for и метода append()
    iterations = 10_000_000
    result = []
    for i in range(iterations):
        result.append(i + 1)
    return result


def list_comprehension():   # с использованием списочного выражения
    iterations = 10_000_000
    return [i + 1 for i in range(iterations)]


def iterations_speed(funcs):
    keys = {}
    for func in funcs:
        start_time = time.perf_counter()
        func()
        end_time = time.perf_counter()
        difference_time = end_time - start_time
        keys[func.__name__] = difference_time
    return (f'Самая быстрая функция вычисления {sorted(keys.items(), key=lambda x: x[1])[0][0]} '
            f'и ее скорость {sorted(keys.items(), key=lambda x: x[1])[0][1]} сек.')


F = (list_comprehension, for_and_append)
print(iterations_speed(F))