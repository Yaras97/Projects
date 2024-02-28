from itertools import filterfalse
objects = [True, False, 'True', 'False', [], ()]
print(*filterfalse(None, objects))


