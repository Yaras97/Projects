positive = [1, 2, 3, 4, 5]
negative = [-1, -2, -3]
combined = [1, 2, -3, 4]
result = map(lambda a, b, c: a + b + c, positive, negative, combined)
print(*result)