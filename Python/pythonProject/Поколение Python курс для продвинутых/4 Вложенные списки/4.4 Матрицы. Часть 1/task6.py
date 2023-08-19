n = int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]
ma = []
for i in range(n):
    for j in range(n):
        if (i >= j and i <= n - 1 - j) or (i <= j and i >= n - 1 - j):
            ma.append(matrix[i][j])
print(max(ma))