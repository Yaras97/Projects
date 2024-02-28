from copy import copy


class Peekable:
    def __init__(self, iterable):
        self.iterable = iter(iterable)

    def peek(self, default=StopIteration):
        iterable = copy(self.iterable)
        item = next(iterable, StopIteration)
        if item is StopIteration and default is StopIteration:
            raise StopIteration
        if item is StopIteration:
            return default
        return item

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterable, StopIteration)
        if item is StopIteration:
            raise StopIteration
        return item


from itertools import islice

iterator = Peekable([1, 2, 3])

print(iterator.peek())
print(list(islice(iterator, 2)))
print(iterator.peek())
print(list(iterator))

try:
    iterator.peek()
except StopIteration:
    print('Пустой итератор')