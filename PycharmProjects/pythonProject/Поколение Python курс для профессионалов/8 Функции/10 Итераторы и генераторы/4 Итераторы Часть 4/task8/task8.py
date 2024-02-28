class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.iterable):
            self.index = 0
        return self.iterable[self.index]


cycle = Cycle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

for _ in range(100):
    print(next(cycle))