# put your python code here
n = int(input())
for i in range(2, n + 1):
    d = n % i
    if d == 0:
        print(i)
        break