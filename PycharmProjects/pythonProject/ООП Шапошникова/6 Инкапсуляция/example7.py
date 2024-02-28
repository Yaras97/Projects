# Если объект содержит скрытые поля и к ним происходит обращение из __setattr__,
# то делать это надо так, как будто обращение происходит не из класса.

class A:
    def __init__(self, n):
        self.a = n
        self.__x = 100 - n

    def __setattr__(self, attr, value):
        if attr in ('a', "_A__x"):
            self.__dict__[attr] = value
        else:
            raise AttributeError


a = A(5)
a._A__x = 3
print(a.__dict__)