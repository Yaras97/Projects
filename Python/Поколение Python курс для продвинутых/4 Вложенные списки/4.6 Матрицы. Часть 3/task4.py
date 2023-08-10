n = int(input())
matrix = [['.'] * n for _ in range(n)]
mat2 = [['*'] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j and matrix[i][j] == '.':
            matrix[i][j], mat2[i][j] = mat2[i][j], matrix[i][j]
        if i + j + 1 == n and matrix[i][j] == '.':
            matrix[i][j], mat2[i][j] = mat2[i][j], matrix[i][j]
        if n // 2 == i and matrix[i][j] == '.':
            matrix[i][j], mat2[i][j] = mat2[i][j], matrix[i][j]
        if n // 2 == j and matrix[i][j] == '.':
            matrix[i][j], mat2[i][j] = mat2[i][j], matrix[i][j]

for i in matrix:
    print(*i)