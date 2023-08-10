n = int(input())
print(*[[int(i) for i in range(1, n + 1)] for i in range(1, n + 1)], sep='\n')