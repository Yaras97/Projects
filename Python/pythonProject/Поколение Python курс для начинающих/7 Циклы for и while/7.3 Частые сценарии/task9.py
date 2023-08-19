n = int(input())
x1 = 0
x2 = 0
for i in range(1, n + 1):
    m = int(input())
    if m > x1:
        x2 = x1
        x1 = m
    elif m > x2:
        x2 = m
print(x1)
print(x2)