n = int(input())
m = set(int(j) for j in input())
for i in range(n - 1):
    m = m & set(int(j) for j in input())
print(*sorted(m))