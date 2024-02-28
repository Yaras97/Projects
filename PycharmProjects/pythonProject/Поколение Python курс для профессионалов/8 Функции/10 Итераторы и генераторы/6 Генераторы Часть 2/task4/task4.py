def all_together(*args):
    return (element for iterable in args for element in iterable)


objects = [range(3), 'bee', [1, 3, 5], (2, 4, 6)]
print(*all_together(*objects))


# from itertools import chain
#
# result = (element for element in chain(*args))