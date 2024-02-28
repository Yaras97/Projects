import calendar, locale

for name in calendar.day_name:
    print(name)


locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
for name in calendar.day_name:
    print(name.title())

names = list(calendar.day_name)
print(names)