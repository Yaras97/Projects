from itertools import groupby
groups = groupby(sorted('aaabbbcccaaaa'))
for _, group in groups:
    print(*group)