from itertools import compress
numbers = [1, -2, 3, 4, -5, -6, 7, 8, -9, -10]
selectors = (i > 0 and i % 2 == 0 for i in numbers)
print(*compress(numbers, selectors))