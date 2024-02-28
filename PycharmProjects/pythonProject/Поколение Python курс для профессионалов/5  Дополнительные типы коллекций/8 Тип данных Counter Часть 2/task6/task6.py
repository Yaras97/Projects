from collections import Counter
counter = Counter(green=10, red=25, blue=5)
print(counter.__dict__)
counter.__dict__['min_value'] = lambda: min(counter.values())
counter.max_value = lambda: max(counter.values())
print(counter.min_value())
print(counter.max_value())