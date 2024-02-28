from collections import ChainMap


def get_value(chainmap, key, from_left=True):
    if key in chainmap:
        if from_left is True:
            return chainmap[key]
        elif from_left is False:
            chainmap.maps.reverse()
            return chainmap[key]
    else:
        return None


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'age'))
