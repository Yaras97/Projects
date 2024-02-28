from collections import ChainMap
letters = ChainMap({'a': 'A', 'b': 'B'}, {'b': 'B', 'c': 'C'})
letters['b'] = 'BB'
print(letters)