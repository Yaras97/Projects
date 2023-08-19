n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]
mat1 = []
mat2 = []
for _ in range(n):
    mat1.append(input().split())
input()
for _ in range(n):
    mat2.append(input().split())

for i in range(n):
    for j in range(m):
        matrix[i][j] = int(mat1[i][j]) + int(mat2[i][j])

for i in matrix:
    print(*i)