from itertools import *


words = input().split()
sorted_func = lambda x: len(x)
result = {word: sorted(other) for word, other in groupby(sorted(words, key=sorted_func), key=sorted_func)}
print(result)
for key, value in result.items():
    print(f'{key} -> {", ".join(value)}')
