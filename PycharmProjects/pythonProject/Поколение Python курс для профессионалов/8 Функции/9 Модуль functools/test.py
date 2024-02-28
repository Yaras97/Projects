from functools import partial


def multiply(a, b):
    '''Функция перемножает два числа и возвращает вычисленное значение.'''
    return a * b


print(multiply.__name__)
print(multiply.__doc__)

double = partial(multiply, 2)
print(double.func.__name__)
print(double.func.__doc__)

