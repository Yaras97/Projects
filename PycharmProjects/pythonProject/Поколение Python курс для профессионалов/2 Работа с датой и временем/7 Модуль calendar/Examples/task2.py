import calendar, locale
locale.setlocale(locale.LC_ALL, 'jp_JP.UTF-8')
print(calendar.calendar(2022, m=4))