from itertools import tee
iter1, iter2 = tee('beegeek')
print(next(iter1))
print(next(iter2))