def get_min_max(iterable):
    result = list(iterable)
    if len(result) == 0:
        return
    return min(result), max(result)


data = iter(['bbb'])

print(get_min_max(data))