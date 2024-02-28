class AttrsIterator:
    def __init__(self, obj):
        self.obj = iter(obj.__dict__.items())

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.obj)


class Kemal:
    def __init__(self):
        self.family = 'cats'
        self.breed = 'british'
        self.master = 'Kemal'


kemal = Kemal()
attrs_iterator = AttrsIterator(kemal)

print(next(attrs_iterator))
print(next(attrs_iterator))
print(next(attrs_iterator))

# class AttrsIterator:
#     def __init__(self, obj):
#         self._obj = list(obj.__dict__.items())
#         self.index = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.index += 1
#         if self.index >= len(self._obj):
#             raise StopIteration
#         return self._obj[self.index]