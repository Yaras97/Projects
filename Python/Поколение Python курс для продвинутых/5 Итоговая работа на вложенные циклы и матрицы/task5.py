n = int(input())
matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][j] = 1
        if i + j + 1 == n:
            matrix[i][j] = 1
        print(matrix[i][j], end=' ')
    print()