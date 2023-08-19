n = int(input())
lst = []
for i in range(n):
    a = input()
    if a not in lst:
        lst.append(a)
print(*lst, sep="\n")