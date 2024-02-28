from collections import ChainMap
letters = ChainMap({'a': 'A'}, {'a': 'A', 'b': 'B', 'c': 'C'})
del letters['a']
del letters['a']
print(letters)