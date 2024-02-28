from collections import Counter
letters1 = Counter('abcd')
letters2 = Counter('abcd')
letters2.update(e=0)
print(letters1 == letters2)