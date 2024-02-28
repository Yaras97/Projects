from collections import UserList

class NumberList(UserList):
    def __init__(self, iterable=()):
        super().__init__()
        for item in iterable:
            if not isinstance(item, (int, float)):
                raise TypeError("Элементами экземпляра класса NumberList должны быть числа")
            self.data.append(item)

    def _check_numeric(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Элементами экземпляра класса NumberList должны быть числа")

    def append(self, item):
        self._check_numeric(item)
        super().append(item)

    def extend(self, iterable):
        for item in iterable:
            self._check_numeric(item)
        super().extend(iterable)

    def insert(self, index, item):
        self._check_numeric(item)
        super().insert(index, item)

    def __setitem__(self, index, value):
        self._check_numeric(value)
        super().__setitem__(index, value)

    def __add__(self, other):
        return NumberList(super().__add__(other))

    def __iadd__(self, other):
        self.extend(other)
        return self


n = NumberList([1, 2, 3])

try:
    n[1] = '5'
except TypeError as e:
    print(e)