class StringList(list):
    def __init__(self, iterable):
        print(iterable)
        super().__init__(str(item) for item in iterable)

    def __setitem__(self, index, item):
        print(item)
        super().__setitem__(index, str(item))

    def __repr__(self):
        return f'{type(self).__name__}({super().__repr__()})'


li = StringList([1, 2, 3])
li[2] = 4

print(li)
