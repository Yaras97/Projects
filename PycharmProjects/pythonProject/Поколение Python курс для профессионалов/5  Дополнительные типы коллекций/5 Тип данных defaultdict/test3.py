from collections import defaultdict


def get_default():
    return 100


data = defaultdict(get_default)
print(data['length'])
print(data['width'])