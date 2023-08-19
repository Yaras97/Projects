n, m = map(int, input().split())
for i in range(n):
    row = [str(i + j * n + 1).ljust(2) for j in range(m)]
    print(*row)




