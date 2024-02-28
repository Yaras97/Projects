def pluck(data, path, default=None):
    for key in path.split('.'):
        if isinstance(data, dict) and key in data:
            data = data[key]
        else:
            return default
    return data


d = {'a': {'b': {'c': {'d': {'e': 4}}}}}

print(pluck(d, 'a.b.c'))