n = int(input())
m = int(input())
matrix = [[i*j for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()