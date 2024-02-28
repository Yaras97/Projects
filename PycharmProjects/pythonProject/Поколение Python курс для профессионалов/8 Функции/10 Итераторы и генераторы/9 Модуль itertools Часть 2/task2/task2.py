def drop_this(iterable, obj):
    iterable = iter(iterable)
    for x in iterable:
        if not x == obj:
            yield x
            break
    for x in iterable:
        yield x


print(list(drop_this([], None)))