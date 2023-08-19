n = input().split()
count = 0
for i in range(len(n)):
    count += int(n[i])
n = '+'.join(n)
print(n, '=', count, sep="")