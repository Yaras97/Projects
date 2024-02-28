n, m = int(input()), int(input())
lst = []
k = m
for i in range(n):
    lst.append([])
    while k != 0:
        lst[i].append(input())
        k -= 1
    k = m
# print(lst)

for i in range(n):
    for j in range(m):
        print(lst[i][j], end=' ')
    print()
