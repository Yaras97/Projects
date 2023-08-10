n = input().split()
lst = []
result = {}
for i in n:
    if i in lst:
        result[i] = result.get(i, 0) + 1
        lst.append(i + "_" + str(result[i]))
    else:
        lst.append(i)
print(*lst)