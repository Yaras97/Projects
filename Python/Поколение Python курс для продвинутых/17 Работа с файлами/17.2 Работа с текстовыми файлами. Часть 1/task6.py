file = open("prices.txt", encoding='utf-8')
lst = []
a = file.read().split()
for i in range(0, len(a)):
    if a[i].isalpha():
        continue
    lst.append(int(a[i]))
s = []
for i in range(0, len(lst), 2):
    s.append(lst[i] * lst[i + 1])
print(sum(s))
file.close()