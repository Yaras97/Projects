m, n = int(input()), int(input())
lst = [input() for i in range(n + m)]
st = set(lst)
lst2 = len(lst) - len(st)
if len(st) - lst2 == 0:
    print('NO')
else:
    print(len(st) - lst2)