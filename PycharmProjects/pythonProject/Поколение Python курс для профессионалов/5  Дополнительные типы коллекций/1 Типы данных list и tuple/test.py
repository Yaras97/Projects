numbers = (1, [2, 3], 4)
numbers[1][0], numbers[1][1] = numbers[1][1], numbers[1][0]
print(numbers)