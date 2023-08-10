import math
n = int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]
for i in range(math.ceil(n/2)):
    for j in range(n):
        matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]

for i in matrix:
    print(*i)