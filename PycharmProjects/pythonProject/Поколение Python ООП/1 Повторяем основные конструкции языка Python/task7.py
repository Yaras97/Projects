def quantify(iterable, predicate=None):
    count = 0
    if predicate == None:
        for i in iterable:
            if bool(i):
                count += 1
    else:
        for i in iterable:
            if predicate(i):
                count += 1

    return count

iterable = iter(['', 1, 0, (), [[]], [], {1: 2}])

print(quantify(iterable, None))


# def quantify(iterable, predicate):
#     if predicate is None:
#         predicate = bool
#     return sum(map(predicate, iterable))