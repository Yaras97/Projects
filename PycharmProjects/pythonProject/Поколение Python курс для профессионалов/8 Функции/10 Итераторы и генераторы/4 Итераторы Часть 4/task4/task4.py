class Fibonacci:
    def __init__(self):
        self.prev, self.current = 1, 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.prev
        self.prev, self.current = self.current, self.prev + self.current
        return result


fibonacci = Fibonacci()

for _ in range(76):
    next(fibonacci)

next(fibonacci)
next(fibonacci)
next(fibonacci)
next(fibonacci)

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))