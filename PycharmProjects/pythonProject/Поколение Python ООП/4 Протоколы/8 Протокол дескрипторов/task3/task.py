class MaxCallsException(Exception):
    pass


class LimitedTakes:
    def __init__(self, times):
        self.times = times
        self.count = 0
        self._value = None

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self._value is None:
            raise AttributeError("Атрибут не найден")
        if self.count >= self.times:
            raise MaxCallsException("Превышено количество доступных обращений")
        self.count += 1
        return self._value

    def __set__(self, instance, value):
        self._value = value

    def __delete__(self, instance):
        self._value = None
        self.count = 0


class Student:
    name = LimitedTakes(3)

student = Student()
student.name = 'Gwen'

print(student.name)
print(student.name)
print(student.name)

try:
    print(student.name)
except MaxCallsException as e:
    print(e)