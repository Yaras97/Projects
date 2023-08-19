n = int(input())
m = {}
for i in range(n):
    for j in range(n - 1, 0, -1):
        if i + j == n and i < j:
            if i % 2 == 1 or j % 2 == 1:
                m[i] = j

s = 0
a = ''
for i, j in sorted(m.items()):
    if i / j > s:
        s = i / j
        a = str(i) + '/' + str(j)
print(a)