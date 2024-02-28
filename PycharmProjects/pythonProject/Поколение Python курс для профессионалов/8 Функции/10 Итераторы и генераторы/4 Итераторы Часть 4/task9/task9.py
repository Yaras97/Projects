from random import choice


class RandomNumbers:
    def __init__(self, left, right, n):
        self.left = left
        self.right = right
        self.n = n
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter == self.n:
            raise StopIteration
        return choice(range(self.left, self.right + 1))


iterator = RandomNumbers(-1000, -900, 4)

print(next(iterator) in range(-1000, -899))
print(next(iterator) in range(-1000, -899))
print(next(iterator) in range(-1000, -899))
print(next(iterator) in range(-1000, -899))

try:
    next(iterator)
except StopIteration:
    print('Error')