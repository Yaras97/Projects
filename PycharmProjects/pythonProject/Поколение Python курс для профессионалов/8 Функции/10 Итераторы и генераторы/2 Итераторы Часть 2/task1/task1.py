def filterfalse(predicate, iterable):
    return filter(lambda x: not predicate(x) if predicate is not None else not x, iterable)


import string
letters = string.ascii_letters
print(letters)
result = filterfalse(lambda char: ord(char) > 75, letters)
print(*result, sep=',')