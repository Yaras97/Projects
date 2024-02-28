digits = '0123456789'
names = []
for _ in range(int(input())):
    name, _ = input().split('@')
    names.append(name)

for _ in range(int(input())):
    name = input()
    count = 0
    while name in names:
        count += 1
        name = name.rstrip(digits) + str(count)
    names.append(name)
    print(f'{name}@beegeek.bzz')