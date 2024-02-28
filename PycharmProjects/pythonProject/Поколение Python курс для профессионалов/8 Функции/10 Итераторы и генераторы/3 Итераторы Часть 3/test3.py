zero_iterator = iter(int, 1)
for i in range(5):
    print(next(zero_iterator))
print(type(zero_iterator))