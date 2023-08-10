mx = -1000000
s = 0
count = 0
for i in range(10):
    x = int(input())
    if x < 0:
        s += x
        count += 1
    if 0 > x >= mx:
        mx = x
if count >= 1:
    print(s)
    print(mx)
else:
    print('NO')