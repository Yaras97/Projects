n = int(input())
lst = [int(input()) for i in range(n)]
cl = int(input())
otv = 'НЕТ'
for i in range(len(lst)):
    if otv == "ДА":
        break
    for j in range(len(lst)):
        if i != j and lst[i] * lst[j] == cl:
            otv = "ДА"
            break
print(otv)