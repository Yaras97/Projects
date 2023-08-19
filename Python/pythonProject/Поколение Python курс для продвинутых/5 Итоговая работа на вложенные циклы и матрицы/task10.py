n, m = map(int, input().split())

i = 0
j = 0
cnt = 1

a = [[0 for _ in range(m)] for _ in range(n)]

while cnt < m * n:
    while j < m - 1 and a[i][j + 1] == 0:
        a[i][j] = cnt
        j += 1
        cnt += 1

    while i < n - 1 and a[i + 1][j] == 0:
        a[i][j] = cnt
        i += 1
        cnt += 1

    while j > 0 and a[i][j - 1] == 0:
        a[i][j] = cnt
        j -= 1
        cnt += 1

    while i > 0 and a[i - 1][j] == 0:
        a[i][j] = cnt
        i -= 1
        cnt += 1

a[i][j] = cnt

for i in range(n):
    for j in range(m):
        print(str(a[i][j]).ljust(3), end=' ')
    print()