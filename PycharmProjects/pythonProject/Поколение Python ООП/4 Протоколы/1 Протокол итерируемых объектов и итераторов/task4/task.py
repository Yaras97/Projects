class SkipIterator:
    def __init__(self, iterable, n):
        self.iterable = tuple(iterable)
        self.n = n
        self.index = -self.n - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += self.n + 1
        if len(self.iterable) > self.index:
            return self.iterable[self.index]
        raise StopIteration


skipiterator = SkipIterator(range(1000), 7)

for _ in range(25):
    next(skipiterator)

print(next(skipiterator))
print(next(skipiterator))
print(next(skipiterator))



