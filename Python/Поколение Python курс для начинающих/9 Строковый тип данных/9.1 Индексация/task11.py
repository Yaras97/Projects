a, b = int(input()), ""
while a > 0:
    b = str(a % 2) + b
    a //= 2
print(b)