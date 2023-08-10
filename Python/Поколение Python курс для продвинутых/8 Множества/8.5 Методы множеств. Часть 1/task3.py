n = list(input())
for i in '.,;:-?!':
    for j in n:
        if i == j:
            n.remove(i)
a = ''.join(n).lower()
n = a.split()
print(len(set(n)))