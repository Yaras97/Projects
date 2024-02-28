from itertools import product
for time in product(range(20), range(60), range(60)):
    print(*time, sep=' : ')