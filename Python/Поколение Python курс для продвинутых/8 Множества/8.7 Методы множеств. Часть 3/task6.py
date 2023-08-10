n = set(int(i) for i in input().split())
m = set(int(i) for i in input().split())
k = set(int(i) for i in input().split())
a = "0 1 2 3 4 5 6 7 8 9 10"
z = set(int(i) for i in a.split())
print(*sorted(z - (n | m | k)))