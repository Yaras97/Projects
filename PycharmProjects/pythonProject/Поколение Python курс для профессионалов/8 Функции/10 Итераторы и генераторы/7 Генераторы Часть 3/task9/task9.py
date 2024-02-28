def with_previous(iterable):
    iterator = iter(iterable)
    previous = None

    for current in iterator:
        yield (current, previous)
        previous = current


print(*with_previous(map(abs, range(-100, 100))))