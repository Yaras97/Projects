from itertools import product
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
product1 = product(numbers, letters)
product2 = product(letters, numbers)
print(*product1)
print(*product1)
print(*product2)
print(product1 == product2)