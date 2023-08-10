n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]
sw = [int(i) for i in input().split()]
for i in range(n):
    matrix[i][sw[0]], matrix[i][sw[1]] = matrix[i][sw[1]], matrix[i][sw[0]]

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()

# for i in matrix:  # можно так
#     print(*i)