class StringList(list):
    def __init__(self, iterable):
        super().__init__(str(item) for item in iterable)

    def __setitem__(self, index, item):
        super().__setitem__(index, str(item))

    def insert(self, index, item):
        super().insert(index, str(item))

    def append(self, item):
        super().append(str(item))

    def extend(self, other):
        print(type(self))
        print(type(other))
        if isinstance(other, type(self)):
            print('hello')
            super().extend(other)
        else:
            super().extend(str(item) for item in other)

    def __repr__(self):
        return f'{type(self).__name__}({super().__repr__()})'


li = StringList([1, 2, 3])
li.append(4)
li.insert(0, 5)
li.extend([6, 7, 8])

print(li)