from itertools import groupby
groups = groupby('aaabbbcccaaaa')
for _, group in groups:
    print(*group)