n = int(input())
x1 = 0
x2 = 1
for i in range(1, n + 1):
    x2 = x1 + x2
    x1 = x2 - x1
    print(x1, end=" ")