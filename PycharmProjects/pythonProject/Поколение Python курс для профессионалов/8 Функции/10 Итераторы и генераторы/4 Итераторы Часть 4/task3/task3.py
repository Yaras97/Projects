class Square:
    def __init__(self, n):
        self.n = n
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter > self.n:
            raise StopIteration
        return self.counter * self.counter


squares = Square(2)

try:
    print(next(squares))
    print(next(squares))
    print(next(squares))
except:
    print('Error')