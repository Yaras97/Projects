import datetime
today = datetime.datetime.now()
future = today + datetime.timedelta(days=28)
f = '%d.%m.%y'
print(today.strftime('Сегодня: ' + f))

print(future.strftime('Через 28 дней будет: ' + f))
