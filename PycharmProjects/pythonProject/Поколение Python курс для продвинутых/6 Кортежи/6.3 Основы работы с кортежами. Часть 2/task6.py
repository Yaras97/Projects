n = int(input())
lst = []
for i in range(n):
    lst.append(input().split())

[print(*i, end='\n') for i in lst]
print()

count = 4
while count != 3:
    for i in range(n):
        if int(lst[i][-1]) >= count:
            print(*lst[i])
    count -= 1