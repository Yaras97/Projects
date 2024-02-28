import sys
from collections import Counter


counter = Counter()
for line in sys.stdin:
    line = line.strip().split()
    counter[line[0]] = int(line[1])

print(sorted(counter.items(), key=lambda x: x[1])[1][0])

