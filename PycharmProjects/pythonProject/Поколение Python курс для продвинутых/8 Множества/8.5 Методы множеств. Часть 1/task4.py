n = input().split()
lst = []
for i in n:
    if i.strip('0') not in lst:
        print('NO')
        lst.append(i)
    else:
        print("YES")