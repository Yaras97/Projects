n = int(input())
result = {}
for i in range(n):
    st = input().split(": ")
    result.setdefault(st[0].lower(), st[1])

m = int(input())
lst = [input().lower() for i in range(m)]

for i in lst:
    if i in result:
        print(result[i])
    else:
        print("Не найдено")