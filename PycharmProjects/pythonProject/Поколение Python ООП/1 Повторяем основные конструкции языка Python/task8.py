from datetime import date, timedelta

year, month = int(input()), int(input())
d = date(year, month, 1)

while d.isoweekday() != 4:
    d += timedelta(days=1)

d += timedelta(days=21)
print(d.strftime('%d.%m.%Y'))