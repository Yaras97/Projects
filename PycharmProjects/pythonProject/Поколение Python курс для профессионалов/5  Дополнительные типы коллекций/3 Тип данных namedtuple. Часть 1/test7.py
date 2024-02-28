from collections import namedtuple
Integer = namedtuple('Integer', ['value', 'even', 'divisors'])
number = Integer(16, True, [1, 2, 4])
number.divisors.extend([8, 16])
print(len(number.divisors))