import random
n = []
for _ in range(7):
    n.append(random.randint(1, 49))
print(*sorted(n))