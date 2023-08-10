n = int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]
for i in range(n):
    for j in range(n):
        print(matrix[n - j - 1][i], end=' ')
    print()