numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
numbers = list(numbers)
for i in range(len(numbers)):
    numbers[i] = sum(numbers[i]) / len(numbers[i])
print(numbers)




