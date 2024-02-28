from collections import ChainMap
from collections import Counter
from collections import defaultdict
from collections import OrderedDict

print(ChainMap())
print(ChainMap({'name': 'Rose', 'age': 17}, {'country': 'USA', 'city': 'Seattle'}))
print(ChainMap(defaultdict(str, a='A', b='B'), OrderedDict(one=1, two=2)))
print(ChainMap(Counter(one=1, two=2), Counter(three=3, four=4)))
print(ChainMap.fromkeys(['math', 'physics', 'chemisty'], 0))
print(ChainMap(Counter(a=4, b=3), OrderedDict(c=1, d=1), defaultdict(e=6, f=11)))
ChainMap(height=100, width=50, thickness=10)