# put your python code here
a = int(input())
if a % 2 == 1:
    print("YES")
elif a % 2 == 0 and 2 <= a <= 5:
    print("NO")
elif a % 2 == 0 and 6 <= a <= 20:
    print("YES")
elif a % 2 == 0 and a > 20:
    print("NO")
