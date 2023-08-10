n = int(input())
matrix = [[int(i) for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if i + j + 1 == n:
            matrix[i][j] = 1
        if i + j + 1 < n:
            matrix[i][j] = 0
        if i + j + 1 > n:
            matrix[i][j] = 2
for i in matrix:
    print(*i)