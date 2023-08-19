k = 0
for i in range(10):
    n = int(input())
    if n % 2 == 0:
        k += 0
    elif n % 2 == 1:
        k += 1
if k == 0:
    print("YES")
elif k > 0:
    print("NO")