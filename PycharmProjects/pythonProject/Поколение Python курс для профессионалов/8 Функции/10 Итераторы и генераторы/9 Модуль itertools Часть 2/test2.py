from itertools import filterfalse
names = ['Timur', 'Arthur', 'Dima', 'Anri']
print(*filterfalse(lambda name: name.startswith('A'), names))