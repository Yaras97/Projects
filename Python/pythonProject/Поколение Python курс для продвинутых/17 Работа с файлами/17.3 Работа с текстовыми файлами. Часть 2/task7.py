import random
with open('first_names.txt') as name, open('last_names.txt') as lstname:
    name = name.read().split()
    lstname = lstname.read().split()
    for _ in range(3):
        print(f'{random.choice(name)} {random.choice(lstname)}')