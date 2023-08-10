# put your python code here

n = int(input())
lst = []
for i in range(n):
    a = int(input())
    lst.append(a)
lst.remove(min(lst))
lst.remove(max(lst))
print(*lst, sep='\n')