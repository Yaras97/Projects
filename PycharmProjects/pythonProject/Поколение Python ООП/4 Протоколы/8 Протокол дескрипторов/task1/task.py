import keyword


class NonKeyword:
    def __init__(self, name):
        self._name = name


    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._name in obj.__dict__:
            return obj.__dict__[self._name]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if keyword.iskeyword(str(value)) and isinstance(value, str):
            raise ValueError("Некорректное значение")
        obj.__dict__[self._name] = value


class Student:
    name = NonKeyword('name')

print(Student.name.__class__)