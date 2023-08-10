n = input().split()
for i in range(len(n)):
    n[i] = int(n[i])

print(*sorted(n))
print(*sorted(n, reverse=True))