from itertools import *

def tabulate(func):
    return starmap(func, zip(count(1)))

func = lambda x: x + 10
values = tabulate(func)

print(next(values))
print(next(values))
print(next(values))


# def tabulate(func):
#     for i in count(1):
#         yield func(i)