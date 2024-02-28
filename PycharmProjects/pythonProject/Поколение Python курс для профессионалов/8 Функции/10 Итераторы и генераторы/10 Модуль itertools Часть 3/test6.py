from itertools import zip_longest
names = ['Timur', 'Arthur', 'Dima']
grades = [100]
print(*zip_longest(names, grades, fillvalue=0))