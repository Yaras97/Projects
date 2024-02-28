n = int(input())
last = 0
last1 = n % 10
count1 = 0
count3 = 0
count2 = 0
count5 = 0
count7 = 1
count05 = 0
while n:
    if last == 3:
        count3 += 1
    last = n % 10
    if last1 == last:
        count1 += 1
    if last % 2 == 0:
        count2 += 1
    if last > 5:
        count5 += last
    if last > 7:
        count7 *= last
    elif last <= 7:
        count7 *= 1
    else:
        count7 = 1
    if last == 0 or last == 5:
        count05 += 1

    n = n // 10
print(count3)
print(count1)
print(count2)
print(count5)
print(count7)
print(count05)
