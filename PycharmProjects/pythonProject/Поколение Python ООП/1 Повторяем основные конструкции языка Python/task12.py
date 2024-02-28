def intersperse(iterable, delimiter):
    first = True
    for item in iterable:
        if not first:
            yield delimiter
        first = False
        yield item


inter = intersperse('beegeek', '!')
print(next(inter))
print(next(inter))
print(*inter)