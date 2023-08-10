n = int(input())
x = []
y = []
for i in range(n):
    a = int(input())
    x.append(a)
    y.append(a**2 + 2 * a + 1)
print(*x, sep="\n")
print()
print(*y, sep="\n")