import random
n = int(input())
[print('Орел') if random.randrange(n) % 2 == 0 else print('Решка') for i in range(n)]









