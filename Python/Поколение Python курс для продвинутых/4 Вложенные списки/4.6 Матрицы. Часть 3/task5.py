n = int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]
ans = 'YES'
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[n - j - 1][n - i - 1]:
            ans = 'NO'
            break
    if ans == 'NO':
        break
print(ans)