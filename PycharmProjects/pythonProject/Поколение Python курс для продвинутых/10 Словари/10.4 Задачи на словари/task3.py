n = sorted([j for i in input().lower().split() for j in i.strip('.,!?:;-')])
m = sorted([j for i in input().lower().split() for j in i.strip('.,!?:;-')])
print("YES" if m == n else 'NO')




