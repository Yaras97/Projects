lst = [int(i) for i in input().split()]
count = 0
for i in range(1, len(lst)):
    if lst[i] > lst[i - 1]:
        count += 1
print(count)