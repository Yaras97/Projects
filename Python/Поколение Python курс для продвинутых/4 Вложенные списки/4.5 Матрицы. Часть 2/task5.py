n = int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]

for i in matrix:
    print(*i)