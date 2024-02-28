from datetime import timedelta, datetime

day = datetime.strptime(input(), '%d.%m.%Y')
for i in range(10):
    print(day.strftime('%d.%m.%Y'))
    day += timedelta(days=i+2)
