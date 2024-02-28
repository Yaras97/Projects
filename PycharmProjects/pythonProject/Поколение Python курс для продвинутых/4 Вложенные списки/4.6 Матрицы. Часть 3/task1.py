lst = input().split()
n = int(input())
lst2 = []
for j in range(n):
    lst2.append([])
    for i in range(j, len(lst), n):
        lst2[-1].append(lst[i])
print(lst2)