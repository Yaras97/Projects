print(range(0) == range(2, 1, 3))
print(range(0, 3, 2) == range(0, 4, 2))

print(*range(0, 3, 2))
print(*range(0, 4, 2))
print(*range(2, 1, 3))
print(*range(0))