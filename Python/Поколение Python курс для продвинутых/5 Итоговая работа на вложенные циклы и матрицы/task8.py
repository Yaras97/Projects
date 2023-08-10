n, m = [int(i) for i in input().split()]
count = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        count += 1
        if i % 2 == 1:
            print(str(count).ljust(3), end=' ')
        if i % 2 == 0:
            print(str(count + m - 2 * j + 1).ljust(3), end=' ')
    print()