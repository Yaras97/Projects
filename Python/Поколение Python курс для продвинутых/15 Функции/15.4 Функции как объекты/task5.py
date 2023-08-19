from math import *
def doit(x, f):
    funcs = {'квадрат': x ** 2,
             'куб': x ** 3,
             'корень': n ** 0.5,
             'модуль': abs(x),
             'синус': sin(x)}
    return funcs[f]
n, do = int(input()), input().lower()
print(doit(n, do))