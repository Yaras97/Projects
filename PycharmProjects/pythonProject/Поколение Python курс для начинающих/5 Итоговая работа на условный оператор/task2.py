# put your python code here
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if (a1 + b1) % 2 == 0 and (a2 + b2) % 2 == 0:
    print("YES")
elif (a1 + b1) % 2 == 1 and (a2 + b2) % 2 == 1:
    print("YES")
else:
    print("NO")
