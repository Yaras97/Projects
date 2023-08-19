lst = [int(i) for i in input().split()]
count = 1
for i in range(len(lst) - 1):
    if lst[i] != lst[i + 1]:
        count += 1
print(count)