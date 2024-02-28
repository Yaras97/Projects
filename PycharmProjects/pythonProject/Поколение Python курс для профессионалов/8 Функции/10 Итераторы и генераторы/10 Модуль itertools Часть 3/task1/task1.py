from itertools import *


def sum_of_digits(iterable):
    iterable = map(str, iterable)
    result = sum(map(int, chain.from_iterable(iterable)))
    return result

numbers = [100, 20, 30, 400, 500, 5]*100000

print(sum_of_digits(numbers))


# def sum_of_digits(iterable):
#     return sum(int(digit) for number in iterable for digit in str(number))