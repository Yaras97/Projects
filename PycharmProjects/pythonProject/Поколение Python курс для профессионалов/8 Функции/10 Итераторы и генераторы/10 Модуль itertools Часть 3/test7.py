from itertools import starmap, pairwise
numbers = [1, 2, 3, 4, 5]
print(*starmap(lambda a, b: a + b, pairwise(numbers)))