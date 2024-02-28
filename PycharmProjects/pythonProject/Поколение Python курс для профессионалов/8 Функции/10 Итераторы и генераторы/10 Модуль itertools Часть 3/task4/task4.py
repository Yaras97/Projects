from itertools import *
def ncycles(iterable, times):
        for i in tee(iterable, times):
            for k in i:
                yield k


print(list(ncycles([], 5)))