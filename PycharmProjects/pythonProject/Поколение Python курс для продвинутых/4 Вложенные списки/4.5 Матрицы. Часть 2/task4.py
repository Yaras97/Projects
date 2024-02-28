n = int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]
ans = 'YES'
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            ans = 'NO'
            break
    if ans == 'NO':
        break
print(ans)