n = [int(input()) for _ in range(int(input()))]
otr = []
nul = []
pol = []
for i in n:
    if i < 0:
        otr.append(i)
    if i == 0:
        nul.append(i)
    if i > 0:
        pol.append(i)
print(*otr, sep='\n')
print(*nul, sep='\n')
print(*pol, sep='\n')