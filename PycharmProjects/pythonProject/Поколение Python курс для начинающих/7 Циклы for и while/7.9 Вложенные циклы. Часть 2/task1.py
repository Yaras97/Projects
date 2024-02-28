count = 0
for i in range(int(input()) + 1):
    for j in range(i):
        count += 1
        print(count, end=" ")
    print()