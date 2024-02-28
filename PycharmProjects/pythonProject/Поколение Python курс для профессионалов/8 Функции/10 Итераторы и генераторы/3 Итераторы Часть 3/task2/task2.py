def is_iterable(obj):
    try:
        iter(obj)
        return True
    except:
        return False

for element in [34, [4, 5], (4, 5), {"a":4}, "dfsdf", 4.5]:
    print(element, 'iterable: ', is_iterable(element))