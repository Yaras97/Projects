from collections import defaultdict


def flip_dict(dict_of_lists):
    new_dict = defaultdict(list)
    for key, value in dict_of_lists.items():
        for i in value:
            new_dict[i].append(key)
    return new_dict


data = data = {1: ['a', 'b', 'c'], 2: ['a', 'b', 'c', 'c'], 3: ['c', 'd', 'a'], 4: ['a', 'b', 'r', 'f'], 5: ['y', 'u', 'e', 'w']}

print(flip_dict(data))