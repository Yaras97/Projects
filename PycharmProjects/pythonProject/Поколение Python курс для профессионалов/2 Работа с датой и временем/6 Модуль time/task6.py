import time


def for_and_append(iterable):    # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result


def list_comprehension(iterable):   # с использованием списочного выражения
    return [elem for elem in iterable]


def list_function(iterable):    # с использованием встроенной функции list()
    return list(iterable)


def iterations_speed(funcs, arg):
    keys = {}
    for func in funcs:
        start_time = time.perf_counter()
        func([arg])
        end_time = time.perf_counter()
        difference_time = end_time - start_time
        keys[func.__name__] = difference_time
    return (f'Самая быстрая функция вычисления {sorted(keys.items(), key=lambda x: x[1])[0][0]} '
            f'и ее скорость {sorted(keys.items(), key=lambda x: x[1])[0][1]} сек.')


F = (list_comprehension, for_and_append, list_function)
print(iterations_speed(F, range(100_000)))