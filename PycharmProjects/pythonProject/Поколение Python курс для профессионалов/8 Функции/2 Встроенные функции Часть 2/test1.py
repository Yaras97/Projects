def hash_as_key(objects):
    hash_dict = {}
    for obj in objects:
        hash_value = hash(obj)
        if hash_value in hash_dict:
            if not isinstance(hash_dict[hash_value], list):
                hash_dict[hash_value] = [hash_dict[hash_value]]
            hash_dict[hash_value].append(obj)
        else:
            hash_dict[hash_value] = obj
    return hash_dict


data = [1, 2, 3, 4, 5, 5]
print(hash_as_key(data))
data = [-1, -2, -3, -4, -5]
print(hash_as_key(data))
data = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]
print(hash_as_key(data))