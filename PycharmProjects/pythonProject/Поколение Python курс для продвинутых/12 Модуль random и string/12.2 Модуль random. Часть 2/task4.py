import random

for i in range(100):
    n = ''
    for j in range(7):
        if j == 0:
            n += str(random.randint(1, 9))
        else:
            n += str(random.randint(0, 9))
    print(n)