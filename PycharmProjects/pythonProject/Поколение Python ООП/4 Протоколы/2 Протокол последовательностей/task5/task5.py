class OrderedSet:
    def __init__(self, iterable=set()):
        self.iterable = set(iterable)
        self.copy = list(iterable)

    def add(self, obj):
        self.iterable.add(obj)

    def discard(self, obj):
        self.iterable.discard(obj)

    def __len__(self):
        return len(self.iterable)

    def __iter__(self):
        yield from self.iterable

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return self.data == other.data
        elif isinstance(other, set):
            return self.set_data == other
        return NotImplemented

print(OrderedSet(['green', 'red', 'blue']) == OrderedSet(['green', 'red', 'blue']))
print(OrderedSet(['green', 'red', 'blue']) == OrderedSet(['red', 'blue', 'green']))
print(OrderedSet(['green', 'red', 'blue']) == {'blue', 'red', 'green'})
print(OrderedSet(['green', 'red', 'blue']) == ['green', 'red', 'blue'])
print(OrderedSet(['green', 'red', 'blue']) == 100)