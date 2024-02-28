from collections import ChainMap


def get_all_values(chainmap, key):
    new_set = set()
    for i_dict in chainmap.maps:
        if key in i_dict:
            new_set.add(i_dict[key])
    return new_set


chainmap = ChainMap({'name': 'Anri'}, {'name': 'Arthur', 'city': 'Almetyevsk'}, {'name': 'Timur', 'age': 29, 'city': 'Moscow'})
result = get_all_values(chainmap, 'city')

print(*sorted(result))