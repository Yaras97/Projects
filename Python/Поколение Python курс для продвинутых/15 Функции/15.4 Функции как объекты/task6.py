def cif(x):
    sm = 0
    for i in str(x):
        sm += int(i)
    return sm

n = input().split()
n.sort(key=cif)
print(*n)