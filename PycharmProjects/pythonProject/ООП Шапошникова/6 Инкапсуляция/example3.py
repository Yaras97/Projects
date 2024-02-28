# Приватными можно делать не только свойства, также методы:
class Natural:
    def __init__(self, n):
        self.__origin = n
        self.number = self.__test()

    def __test(self):
        if type(self.__origin) is int and self.__origin > 0:
            return self.__origin
        else:
            print(f'Значение {self.__origin} было преобразовано к 1')
            return 1


a = Natural(34)
b = Natural(-250)
c = Natural('Hello')

print(a.number, b.number, c.number)