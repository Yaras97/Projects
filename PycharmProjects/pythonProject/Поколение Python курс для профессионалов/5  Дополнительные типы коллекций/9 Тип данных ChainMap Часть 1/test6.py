from collections import ChainMap, defaultdict
info = ChainMap({'hobby': 'math', 'country': 'USA', 'city': 'Seattle'},
defaultdict(int, {'name': 'Rose', 'age': 17}))
print(info['hobby'])