from itertools import cycle

class CyclicList:
    def __init__(self, iterable=[]):
        self.iterable = list(iterable)

    def append(self, obj):
        self.iterable.append(obj)

    def pop(self, index=-1):
        return self.iterable.pop(index)

    def __len__(self):
        return len(self.iterable)

    def __getitem__(self, key):
        return self.iterable[key % len(self.iterable)]

    def __iter__(self):
        yield from cycle(self.iterable)


cyclic_list = CyclicList()
cyclic_list.append(1)

for index, elem in enumerate(cyclic_list):
    if index > 6:
        break
    print(elem, end=' ')