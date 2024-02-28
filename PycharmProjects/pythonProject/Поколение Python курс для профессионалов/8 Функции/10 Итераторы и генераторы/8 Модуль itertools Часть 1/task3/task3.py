from itertools import *

def alnum_sequence():
    for i in cycle(enumerate(tuple(chr(let) for let in range(ord('A'), ord('Z') + 1)), 1)):
        yield from i


alnum = alnum_sequence()

for _ in range(100_000):
    next(alnum)

print(next(alnum))
print(next(alnum))
print(next(alnum))
print(next(alnum))