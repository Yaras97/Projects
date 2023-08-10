n, m = set(int(i) for i in input().split()), set(int(i) for i in input().split())
# print(print(*sorted(n & m, reverse=True)) if len(n & m) != 0 else print("BAD DAY"))
if len(n & m) != 0:
    print(*sorted(n & m, reverse=True))
else:
    print("BAD DAY")