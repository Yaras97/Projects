n = input().split()
lst = [[]]
a = 1
while a != len(n) + 1:
    for i in range(len(n)):
        if len(n[i:i+a]) == a:
            lst.append(n[i:i+a])
    a += 1
print(lst)