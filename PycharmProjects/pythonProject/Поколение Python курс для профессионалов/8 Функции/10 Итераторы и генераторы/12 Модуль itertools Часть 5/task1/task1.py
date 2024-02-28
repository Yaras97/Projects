from itertools import *
for i in sorted(set(permutations((list('aab')), 3))):
    print(*i, sep='')