n = int(input())
m = n % 10
answer = 'YES'
while n != 0 and answer == "YES":
    if m != n % 10:
        answer = 'NO'
    n = n // 10
print(answer)