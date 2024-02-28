class NonNegativeInteger:
    def __init__(self, name, default=None):
        self.name = name
        self.default = default
        self._value = default

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self._value is None:
            if self.default is None:
                raise AttributeError("Атрибут не найден")
            return self.default
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Некорректное значение")
        self._value = value

    def __delete__(self, instance):
        self._value = None


class Student:
    score = NonNegativeInteger('score')

print(Student.score.__class__)