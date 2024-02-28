def dict_travel(nested_dicts, parent_keys=None):
    if parent_keys is None:
        parent_keys = []

    for key, value in sorted(nested_dicts.items()):
        current_keys = parent_keys + [key]
        current_key_str = ".".join(current_keys)

        if isinstance(value, dict):
            dict_travel(value, parent_keys=current_keys)
        else:
            print(f"{current_key_str}: {value}")


data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}

dict_travel(data)
