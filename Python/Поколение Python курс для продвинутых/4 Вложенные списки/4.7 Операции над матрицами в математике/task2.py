n1, m1 = [int(i) for i in input().split()]
mat1 = [[int(i) for i in input().split()] for _ in range(n1)]
input()
n2, m2 = [int(i) for i in input().split()]
mat2 = [[int(i) for i in input().split()] for _ in range(n2)]
matrix = [[0] * m2 for i in range(n1)]
for i in range(n1):
    for j in range(m2):
        count = 0
        for k in range(m1):
            count += mat1[i][k] * mat2[k][j]
        matrix[i][j] = count

for i in matrix:
    print(*i)