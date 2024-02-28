from functools import singledispatchmethod

class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(obj):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @format.register(int)
    @staticmethod
    def int_format(obj):
        print(f'Целое число: {obj}')

    @format.register(float)
    @staticmethod
    def int_format(obj):
        print(f'Вещественное число: {obj}')

    @format.register(list)
    @staticmethod
    def int_format(obj):
        print(f"Элементы списка: {', '.join(map(str, obj))}")

    @format.register(tuple)
    @staticmethod
    def int_format(obj):
        print(f"Элементы кортежа: {', '.join(map(str, obj))}")

    @format.register(dict)
    @staticmethod
    def int_format(obj):
        print(f"Пары словаря: {', '.join(map(str, obj.items()))}")

Formatter.format({'Cuphead': 1, 'Mugman': 3})
Formatter.format({1: 'one', 2: 'two'})
Formatter.format({1: True, 0: False})