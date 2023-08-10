a, b = int(input()), int(input())
k = 0
for i in range(a, b + 1):
    if i**3 % 10 == 4:
        k += 1
    elif i**3 % 10 == 9:
        k += 1
print(k)