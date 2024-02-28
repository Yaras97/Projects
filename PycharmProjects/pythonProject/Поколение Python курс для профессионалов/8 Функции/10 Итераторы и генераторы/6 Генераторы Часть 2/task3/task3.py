def count_iterable(iterable):
    return len(list(i for i in iterable))


data = filter(None, range(100_000_001))

print(count_iterable(data))