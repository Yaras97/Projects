from collections import ChainMap
letters = ChainMap({'a': 'A', 'b': 'B'},
                   {'c': 'C'},
                   {'d': 'D', 'e': 'E'})
letters.clear()
print(letters)