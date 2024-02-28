def around(iterable):
    iterator = iter(iterable)
    previous = None
    try:
        current = next(iterator)
    except StopIteration:
        return

    for next_element in iterator:
        yield (previous, current, next_element)
        previous, current = current, next_element

    yield (previous, current, None)


data = map(abs, range(-100, 100))

print(*around(data))