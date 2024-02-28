from itertools import *


def max_pair(iterable):
    result = max(map(lambda x: x[0] + x[1], pairwise(iterable)))
    return result

iterator = iter([11, 10, 19, 1, 12, 100, 1, 13, 107])

print(max_pair(iterator))