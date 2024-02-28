from itertools import *

def take_nth(iterable, n):
    return next(islice(iterable, n-1, None), None)


iterator = tuple('stepik')

print(take_nth(iterator, 6))