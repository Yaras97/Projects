def drop_while_negative(iterable):
    iterable = iter(iterable)
    for x in iterable:
        if x >= 0:
            yield x
            break
    for x in iterable:
        yield x


iterator = iter([])

print(list(drop_while_negative(iterator)))