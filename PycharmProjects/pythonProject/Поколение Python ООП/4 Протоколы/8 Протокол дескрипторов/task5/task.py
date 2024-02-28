import random

class RandomNumber:
    def __init__(self, start, end, cache=False):
        self.start = start
        self.end = end
        self.cache = cache
        self._value = None

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self._value is None or not self.cache:
            self._value = random.randint(self.start, self.end)
        return self._value

    def __set__(self, instance, value):
        raise AttributeError("Изменение невозможно")

    def __delete__(self, instance):
        self._value = None


class MagicPoint:
    x = RandomNumber(0, 5, True)
    y = RandomNumber(0, 5)
    z = RandomNumber(0, 5)

magicpoint = MagicPoint()
value = magicpoint.x

print(magicpoint.x == value)
print(magicpoint.x == value)
print(magicpoint.x == value)