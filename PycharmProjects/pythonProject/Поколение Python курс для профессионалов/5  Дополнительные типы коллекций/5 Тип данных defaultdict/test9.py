from collections import defaultdict
data = defaultdict()
for func in reversed([list, int, dict, set]):
    data.default_factory = func
print(data['key'])