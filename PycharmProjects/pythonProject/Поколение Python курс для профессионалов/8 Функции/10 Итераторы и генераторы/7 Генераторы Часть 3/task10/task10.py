def pairwise(iterable):
    iterator = iter(iterable)

    for current in iterator:
        next_element = next(iterator, None)
        yield (current, next_element)


data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')

print(*pairwise(data))