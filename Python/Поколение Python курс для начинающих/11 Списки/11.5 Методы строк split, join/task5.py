n = input().split(".")
count = 0
for i in n:
    if 0 <= int(i) <= 255:
        count += 1
    else:
        count -= 1
if count == 4:
    print("ДА")
else:
    print("НЕТ")