n = int(input())
matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i <= j and i <= n - 1 - j:
            matrix[i][j] = 1
        if i >= j and i >= n - 1 - j:
            matrix[i][j] = 1
        print(matrix[i][j], end=' ')
    print()
