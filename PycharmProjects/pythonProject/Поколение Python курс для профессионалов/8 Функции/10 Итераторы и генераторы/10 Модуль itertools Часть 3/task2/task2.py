def is_rising(iterable):
    if list(iterable) == sorted(iterable):
        return True
    else:
        return False

iterator = iter([1, 1, 1, 2, 3, 4])
print(is_rising(iterator))


# from itertools import tee, pairwise
#
# def pairwise(iterable):
#     a, b = tee(iterable)
#     next(b, None)
#     return zip(a, b)
#
# def is_rising(iterable):
#     return all(x < y for x, y in pairwise(iterable))