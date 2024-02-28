class DictItemsIterator:
    def __init__(self, data):
        self.data = data
        self.keys = list(data)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.keys:
            raise StopIteration
        key = self.keys.pop(0)
        value = self.data[key]
        return key, value


pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})
print(*pairs)
