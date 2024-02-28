class NumberNotInRangeError(Exception):
    pass


try:
    number = int('3999')
    if not 4000 < number < 8000:
        raise NumberNotInRangeError('Число из недопустимого диапазона')
    print(number)
except NumberNotInRangeError as e:
    print(e)
