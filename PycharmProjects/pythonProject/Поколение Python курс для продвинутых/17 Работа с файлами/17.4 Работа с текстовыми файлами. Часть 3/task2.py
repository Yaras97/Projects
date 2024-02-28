import random
with open('random.txt', 'w') as file:
    for i in range(25):
        file.write(str(random.randrange(111, 778)) + '\n')
