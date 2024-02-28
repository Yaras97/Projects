from itertools import zip_longest
names = ['Timur', 'Arthur']
grades = [100, 99, 200]
print(*zip_longest(names, grades))