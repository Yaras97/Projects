n1 = set(int(i) for i in input().split())
n2 = set(int(i) for i in input().split())
n3 = set(int(i) for i in input().split())
print(*sorted(n3 - ((n1 | n2) & n3), reverse=True))




