class AdvancedTuple(tuple):
    def __add__(self, other):
        if isinstance(other, (list, tuple)):
            return AdvancedTuple(super().__add__(tuple(other)))
        elif hasattr(other, '__iter__'):
            return AdvancedTuple(super().__add__(tuple(other)))
        else:
            raise TypeError("Unsupported operand type(s) for +")

    def __radd__(self, other):
        if isinstance(other, (list, tuple)):
            return AdvancedTuple(tuple(other).__add__(self))
        elif hasattr(other, '__iter__'):
            return AdvancedTuple(tuple(other).__add__(self))
        else:
            raise TypeError("Unsupported operand type(s) for +")

    def __iadd__(self, other):
        if isinstance(other, (list, tuple)):
            return AdvancedTuple(super().__add__(tuple(other)))
        elif hasattr(other, '__iter__'):
            return AdvancedTuple(super().__add__(tuple(other)))
        else:
            raise TypeError("Unsupported operand type(s) for +")

    def __new__(cls, iterable=()):
        return super().__new__(cls, iterable)


advancedtuple = AdvancedTuple([1, 2, 3])

print(advancedtuple + (4, 5))
print(advancedtuple + [4, 5])
print({'a': 1, 'b': 2} + advancedtuple)