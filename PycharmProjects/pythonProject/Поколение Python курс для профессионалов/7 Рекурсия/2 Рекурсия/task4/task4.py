import sys

numbers = [int(i) for i in sys.stdin]


def counter(n, c=0):
    if n[c] != 0:
        counter(n, c+1)
        print(n[c])
    else:
        print(n[c])


counter(numbers)
