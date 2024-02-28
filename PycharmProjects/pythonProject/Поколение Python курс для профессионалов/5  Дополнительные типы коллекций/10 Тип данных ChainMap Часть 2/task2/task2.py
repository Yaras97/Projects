from collections import ChainMap


def deep_update(chainmap, key, value):
    if len(chainmap) != 0:
        for i_dict in chainmap.maps:
            if key in i_dict:
                i_dict[key] = value
            elif key not in chainmap:
                chainmap[key] = value
        return chainmap
    else:
        return None


chainmap = ChainMap({})

print(deep_update(chainmap, 'city', 'Moscow'))
