def get_value(nested_dicts, key):
    if key in nested_dicts:
        return nested_dicts[key]
    for k, v in nested_dicts.items():
        if type(v) is dict:
            v = get_value(v, key)
            if v is not None:
                return v


data = {'a': 11, 'b': {'c': 34, 'd': 2224, 'e': {'f': 5133, 'g': 609}}}

print(get_value(data, 'g'))