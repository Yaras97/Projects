a, b, c = input(), input(), input()
a1 = len(a)
b1 = len(b)
c1 = len(c)
if (2 * b1 - c1 - a1) * (2 * c1 - b1 - a1) * (2 * a1 - b1 - c1) == 0:
    print("YES")
else:
    print("NO")