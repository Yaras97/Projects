# put your python code here
a = int(input())
if a >= 1000 and a <= 9999:
    if a % 7 == 0 or a % 17 == 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')