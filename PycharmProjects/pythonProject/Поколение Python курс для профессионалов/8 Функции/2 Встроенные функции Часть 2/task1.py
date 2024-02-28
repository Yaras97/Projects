def hash_as_key(objects):
    hash_dict = {}
    for obj in objects:
        hash_value = hash(obj)
        if obj == -1 or obj == -2:
            if -1 and -2 in objects:
                hash_dict[hash_value] = [-1, -2]
        if objects.count(obj) == 1:
            hash_dict[hash_value] = obj
        else:
            hash_dict[hash_value] = [obj] * objects.count(obj)
    return hash_dict


data = [1, 2, 3, 4, 5, 5]
print(hash_as_key(data))

data = [-1, -2, -3, -4, -5]
print(hash_as_key(data))