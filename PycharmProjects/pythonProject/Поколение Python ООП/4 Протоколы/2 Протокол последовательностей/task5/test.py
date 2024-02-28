class OrderedSet:
    def __init__(self, iterable=None):
        self.data = []
        self.set_data = set()
        if iterable is not None:
            for item in iterable:
                self.add(item)

    def add(self, item):
        if item not in self.set_data:
            self.data.append(item)
            self.set_data.add(item)

    def discard(self, item):
        if item in self.set_data:
            self.data.remove(item)
            self.set_data.remove(item)

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def __contains__(self, item):
        return item in self.set_data

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return self.data == other.data
        elif isinstance(other, set):
            return self.set_data == other
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

orderedset = OrderedSet([1, 2, 3, 4])
print(orderedset.__eq__(1))
print(orderedset.__ne__(1.1))