from math import *
# объявление функции
def get_circle(radius):
    c = 2 * pi * r
    s = pi * r ** 2
    return c, s

# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)