n = input()
file = open(n)
for line in file:
    print(line.rstrip())
file.close()
