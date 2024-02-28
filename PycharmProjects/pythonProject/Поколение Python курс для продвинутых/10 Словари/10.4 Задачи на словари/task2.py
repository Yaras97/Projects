n = list(input())
m = list(input())
lst = {}
lst2 = {}
for i in n:
    lst[i] = lst.get(i, 0) + 1
for i in m:
    lst2[i] = lst2.get(i, 0) + 1

if lst == lst2:
    print("YES")
else:
    print("NO")