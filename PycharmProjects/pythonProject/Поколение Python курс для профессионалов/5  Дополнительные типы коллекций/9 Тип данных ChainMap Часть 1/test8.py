from collections import ChainMap
letters = ChainMap({'a': 'A'}, {'b': 'B', 'c': 'C'})
letters['b'] = 'BB'
letters['c'] = 'CC'
print(letters)