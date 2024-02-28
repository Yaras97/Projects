from collections import *


class DefaultList(UserList):
    def __init__(self, iterable=(), default=None):
        super().__init__(iterable)
        self.default = default

    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except IndexError:
            return self.default

defaultlist = DefaultList([1, 2, 3])
print(defaultlist[-1])
print(defaultlist[-2])
print(defaultlist[-3])