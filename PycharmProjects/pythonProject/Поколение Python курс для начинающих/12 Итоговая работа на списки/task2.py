L = [int(i) for i in list(input().split())]
M = [int(i) for i in list(input().split())]
lst = []
for i in range(len(L)):
    lst.append(L[i] + M[i])

print(*lst)