n = input().split()
res = {}
for i in n:
    res[i] = res.get(i, 0) + 1
    print(res[i], end=' ')