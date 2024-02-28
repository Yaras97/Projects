from itertools import takewhile
numbers = [1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1]
print(*takewhile(lambda x: x < 5, numbers))