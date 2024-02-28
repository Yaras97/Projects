from collections import ChainMap, defaultdict
info = ChainMap(defaultdict(int, {'name': 'Rose', 'age': 17}),
{'hobby': 'math', 'country': 'USA', 'city': 'Seattle'})
print(info['hobby'])