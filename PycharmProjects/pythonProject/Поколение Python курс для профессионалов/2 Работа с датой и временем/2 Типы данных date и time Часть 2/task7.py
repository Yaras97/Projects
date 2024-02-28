from datetime import date
a = sorted([date.fromisoformat(input()) for _ in range(int(input()))])
[print(i.strftime('%d/%m/%Y')) for i in a]
