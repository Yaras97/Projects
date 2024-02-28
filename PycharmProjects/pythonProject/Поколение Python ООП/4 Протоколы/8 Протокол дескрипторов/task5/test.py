import random

class RandomNumber:
    def __init__(self, start, end, cache=False):
        self.start = start
        self.end = end
        self.cache = cache

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if not hasattr(instance, "_cached_values"):
            instance._cached_values = {}
        if self.cache and self.name in instance._cached_values:
            return instance._cached_values[self.name]
        value = random.randint(self.start, self.end)
        if self.cache:
            instance._cached_values[self.name] = value
        return value

    def __set__(self, instance, value):
        raise AttributeError("Изменение невозможно")

    def __delete__(self, instance):
        if hasattr(instance, "_cached_values") and self.name in instance._cached_values:
            del instance._cached_values[self.name]