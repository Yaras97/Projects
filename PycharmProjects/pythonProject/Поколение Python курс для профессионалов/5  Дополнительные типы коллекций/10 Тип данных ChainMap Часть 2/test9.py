from collections import ChainMap

chainmap1 = ChainMap({'a': 1}, {'b': 2}, {'c': 3})
chainmap2 = ChainMap({'a': 1, 'b': 2}, {'c': 3}, {'a': 10, 'b': 20, 'c': 30})
print(chainmap1 == chainmap2)
