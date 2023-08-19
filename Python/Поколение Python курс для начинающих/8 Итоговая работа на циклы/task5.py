n = int(input())
kolvo = len(str(n))
last = 0
while kolvo != 2:
    kolvo -= 1
    last = n % 10
    n = n // 10

print(last)