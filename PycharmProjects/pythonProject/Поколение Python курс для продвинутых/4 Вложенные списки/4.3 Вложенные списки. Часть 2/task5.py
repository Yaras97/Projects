n = input().split()
lst = []
st = ''
for i in n:
    if st != i:
        lst.append([i])
    else:
        lst[-1].append(i)
    st = i
print(lst)