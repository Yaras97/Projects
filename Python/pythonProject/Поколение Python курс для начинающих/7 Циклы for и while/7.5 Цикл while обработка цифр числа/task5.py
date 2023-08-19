n = int(input())
per = 1
pre_per = 0
while n:
    pre_per = per
    per = n % 10
    n = n // 10
print(pre_per)