n = [i.strip('.,!?:;-') for i in input().lower().split()]
result = {}
for i in n:
    result[i] = result.get(i, 0) + 1
mini = min([result[i] for i in result])
lst = []
for i in result:
    if result[i] == mini:
        lst.append(i)
print(min(lst))