from itertools import groupby
numbers = [1, 1, 1, 7, 7, 7, 7, 15, 7, 7, 7]
key_func = lambda num: num < 10
print(sorted(numbers, key=key_func))
group_iter = groupby(sorted(numbers, key=key_func), key=key_func)
for key, values in group_iter:
    print(f'{key}: {list(values)}')