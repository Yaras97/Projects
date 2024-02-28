import random


class Dice:
    def __init__(self, sides):
        self.sides = sides

    def __call__(self):
        return random.choice(range(1, self.sides + 1))

kingdice = Dice(20)
print(callable(kingdice))