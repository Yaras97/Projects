numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)
del numbers[4]
print(list(iterator))