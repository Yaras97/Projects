from collections import defaultdict
data = defaultdict(list)
print(data['key1'])
data.default_factory = dict
print(data['key2'])
data.default_factory = tuple
print(data['key3'])