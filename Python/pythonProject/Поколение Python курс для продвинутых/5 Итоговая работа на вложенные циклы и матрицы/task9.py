n, m = [int(i) for i in input().split()]
lst = [[0] * m for _ in range(n)]
count = 0
for k in range(n*m):
    for i in range(n):
        for j in range(m):
            if i + j == k:
                count += 1
                lst[i][j] = count

for i in range(n):
    for j in range(m):
        print(str(lst[i][j]).ljust(2), end=' ')
    print()