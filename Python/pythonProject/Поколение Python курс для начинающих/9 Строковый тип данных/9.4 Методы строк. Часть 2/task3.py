n = int(input())
count = 0
while n != 0:
    a = input().count('11')
    if a >= 3:
        count += 1
    n -= 1
print(count)