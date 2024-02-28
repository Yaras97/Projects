class BoundedRepeater:
    def __init__(self, obj, times):
        self.obj = obj
        self.times = times
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter > self.times:
            raise StopIteration
        return self.obj


repeater = BoundedRepeater(1, 10)

print(list(repeater))