n = int(input())
print(*[[int(j) for j in range(1, i + 1)]for i in range(1, n + 1)], sep='\n')