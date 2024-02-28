# Вам доступны три реализации функции, которая вычисляет факториал числа n:
# встроенная из модуля math
# рекурсивная
# итеративная
# Выясните, какая функция быстрее вычислит факториал числа 900.
# Примечание. Реализации функций:


from math import factorial  # функция из модуля math
import time


def factorial_recurrent(n):     # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)


def factorial_classic(n):   # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


def factorial_speed(funcs, arg):
    keys = {}
    for func in funcs:
        start_time = time.perf_counter()
        func(arg)
        end_time = time.perf_counter()
        difference_time = end_time - start_time
        keys[func.__name__] = difference_time
    return (f'Самая быстрая функция вычисления факториала {sorted(keys.items(), key=lambda x: x[1])[0][0]} '
            f'и ее скорость {sorted(keys.items(), key=lambda x: x[1])[0][1]} сек.')


F = (factorial_recurrent, factorial_classic, factorial)
print(factorial_speed(F, 900))
