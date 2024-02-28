def roundrobin(*args):
    iterators = [iter(iterable) for iterable in args]
    active_iterators = len(iterators)

    while active_iterators > 0:
        for iterator in iterators:
            try:
                yield next(iterator)
            except StopIteration:
                active_iterators -= 1

print(*roundrobin('abc', 'd', 'ef'))