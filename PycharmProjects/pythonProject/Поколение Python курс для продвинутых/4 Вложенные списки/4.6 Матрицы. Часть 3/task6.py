n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
ans = 'YES'
for i in range(n):
    lst = []
    lst2 = []
    for j in range(n):
        lst.append(matrix[i][j])
        lst2.append(matrix[j][i])
    if sorted(lst) != sorted(lst2):
        ans = 'NO'
        break
    if sorted(lst) != [int(i) for i in range(1, n + 1)]:
        ans = 'NO'
        break
    if sorted(lst2) != [int(i) for i in range(1, n + 1)]:
        ans = 'NO'
        break
print(ans)