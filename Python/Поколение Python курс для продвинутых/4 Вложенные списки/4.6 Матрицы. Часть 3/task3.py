n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
mat2 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        mat2[i][j] = matrix[j][i]
for i in mat2:
    print(*i)