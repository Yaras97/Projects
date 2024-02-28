class Xrange:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.index = self.start - self.step

    def __iter__(self):
        return self

    def __next__(self):
        self.index += self.step
        if self.index >= self.end:
            raise StopIteration
        return self.index


xrange = Xrange(5.1, 55, 1.1)

print(tuple(xrange))