n = int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]
d1 = 0
d2 = 0
count = 0
count2 = 0
otv = 'YES'
for i in range(n):
    if count != count2:
        otv = 'NO'
        break
    count = 0
    count2 = 0
    for j in range(n):
        if matrix[i][j] > n**2:
            otv = 'NO'
            break
        if matrix[i][j] == 0:
            otv = 'NO'
            break
        if i != j:
            if matrix[i][j] == matrix[j][i]:
                otv = 'NO'

        if i == j:
            d1 += matrix[i][j]
        if i + j + 1 == n:
            d2 += matrix[i][j]
        count += matrix[i][j]
        count2 += matrix[j][i]

if d1 != d2:
    otv = 'NO'
if d1 != d2 != count2 != count:
    otv = 'NO'
print(otv)
