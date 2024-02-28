from functools import singledispatchmethod

class Processor:

    @singledispatchmethod
    @staticmethod
    def process(obj):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @process.register(str)
    @staticmethod
    def str_process(obj):
        return obj.upper()

    @process.register(int)
    @staticmethod
    def int_process(obj):
        return obj * 2

    @process.register(float)
    @staticmethod
    def float_process(obj):
        return obj * 2

    @process.register(list)
    @staticmethod
    def list_tuple_process(obj):
        return sorted(obj)

    @process.register(tuple)
    @staticmethod
    def tuple_process(obj):
        return tuple(sorted(obj))

objects = [None, {1, 2, 3}, {1: 'one', 2: 'two'}]

for obj in objects:
    try:
        Processor.process(obj)
    except TypeError as e:
        print(e)