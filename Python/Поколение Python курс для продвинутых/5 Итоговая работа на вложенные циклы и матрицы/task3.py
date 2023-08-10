n, m = [int(i) for i in input().split()]
[print(*[str(i * m + j * 1).ljust(2) for j in range(1, m + 1)]) for i in range(n)]





