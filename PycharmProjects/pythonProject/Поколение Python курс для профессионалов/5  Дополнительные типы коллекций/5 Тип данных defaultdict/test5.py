from collections import defaultdict


def get_default(x):
    return abs(x)


data = defaultdict(get_default)
print(data[-100])