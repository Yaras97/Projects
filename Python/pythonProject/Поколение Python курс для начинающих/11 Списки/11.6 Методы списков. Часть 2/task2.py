num = input().split()
for i in range(len(num)):
    num[i] = int(num[i])
imax = num.index(max(num))
imin = num.index(min(num))
num[imin], num[imax] = num[imax], num[imin]
print(*num)