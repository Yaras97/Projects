n = int(input())
lenght = len(str(n))
while n > 0 and lenght != 1:
    summ = 0
    while n > 0:
        last = n % 10
        summ += last
        n = n // 10
    lenght = len(str(summ))
    n = summ
print(n)