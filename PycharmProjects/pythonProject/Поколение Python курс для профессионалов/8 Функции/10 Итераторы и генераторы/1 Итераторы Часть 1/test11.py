numbers = filter(None, [0, 1, 2, 3])
next(numbers)
next(numbers)
next(numbers)
try:
    print(next(numbers))
except StopIteration as e:
    print('Error')