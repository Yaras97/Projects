n = int(input())
for i in range(1, n + 1):
    if i == 1:
        print("*" * 19)
    elif i == n:
        print("*" * 19)
    else:
        print("*", " " * 15, "*")