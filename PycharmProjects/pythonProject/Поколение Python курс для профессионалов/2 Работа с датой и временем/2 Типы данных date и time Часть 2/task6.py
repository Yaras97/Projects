from datetime import date
n = date.fromisoformat(input())
m = date.fromisoformat(input())
a = min(n, m)
print(a.strftime('%d-%m (%Y)'))
