n = int(input())
dl = []
for i in range(1,n + 1):
    if n % i == 0:
        dl += [i]
print(dl)