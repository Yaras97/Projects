def first_true(iterable, predicate):
    if predicate is None:
        predicate = bool
    for x in iterable:
        if predicate(x):
            return x
    return None

numbers = iter([])

print(first_true(numbers, lambda num: num == 200))


