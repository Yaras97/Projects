import time

F = (min, max, sum)


def get_the_fastest_func(funcs, *args):
    keys = {}
    for func in funcs:
        start_time = time.perf_counter()
        func([*args])
        end_time = time.perf_counter()
        difference_time = end_time - start_time
        keys[func.__name__] = difference_time
    return (f'Самая быстрая функция вычисления {sorted(keys.items(), key=lambda x: x[1])[0][0]} '
            f'и ее скорость {sorted(keys.items(), key=lambda x: x[1])[0][1]} сек.')


print(get_the_fastest_func(F, 1, 2, 3))
