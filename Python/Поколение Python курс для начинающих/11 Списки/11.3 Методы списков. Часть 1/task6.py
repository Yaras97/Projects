n = int(input())
dl = 0
lst = []
for i in range(n):
    num = int(input())
    dl += num
    lst.append(dl)
    dl = num
print(lst[1:])