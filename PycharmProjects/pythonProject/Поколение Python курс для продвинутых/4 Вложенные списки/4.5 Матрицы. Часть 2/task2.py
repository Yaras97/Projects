n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]
a = max(max(matrix, key=max))
for i in range(n):
    for j in range(m):
        if matrix[i][j] == a:
            break
    if matrix[i][j] == a:
        break
print(i, j)