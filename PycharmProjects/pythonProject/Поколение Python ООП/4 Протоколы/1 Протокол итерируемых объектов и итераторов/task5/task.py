import random


class RandomLooper:
    def __init__(self, *args):
        self.args = [elem for iterable in args for elem in iterable]
        random.shuffle(self.args)
        self.args = iter(self.args)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.args)


randomlooper = RandomLooper(['red', 'blue', 'green', 'purple'])

answer = [next(randomlooper) for _ in range(4)]
print(answer)