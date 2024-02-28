from collections import UserDict


class TwoWayDict(UserDict):
    def __setitem__(self, key, value):
        self.data.__setitem__(value, key)
        self.data.__setitem__(key, value)


d = TwoWayDict()

for i in range(100):
    d[i] = i + 100

print(d)