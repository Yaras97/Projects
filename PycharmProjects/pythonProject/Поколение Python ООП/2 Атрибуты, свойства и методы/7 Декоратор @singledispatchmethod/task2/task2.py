from functools import singledispatchmethod

class Negator:

    @singledispatchmethod
    @staticmethod
    def neg(obj):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def int_float_neg(obj):
        return -obj

    @neg.register(bool)
    @staticmethod
    def bool_neg(obj):
        return not obj


not_supported = [[1, 2, 3], (4, 5, 6), {1: 'one'}, {10, 11, 12}, 'Timothy John «Tim» Berners-Lee']

for item in not_supported:
    try:
        Negator.neg(item)
    except TypeError as e:
        print(e)