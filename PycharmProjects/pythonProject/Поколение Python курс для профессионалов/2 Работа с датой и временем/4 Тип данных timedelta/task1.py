# Дополните приведенный ниже код, чтобы он прибавил к объекту datetime(2021, 11, 4, 13, 6)
# одну неделю и 1212 часов и вывел результат в формате DD.MM.YYYY HH:MM:SS.

from datetime import datetime, timedelta

dt = datetime(2021, 11, 4, 13, 6) + timedelta(days=7, hours=1212)

print(dt.strftime('%d.%m.%y %H:%M:%S'))
print(dt)


# Дополните приведенный ниже код, чтобы он вывел количество дней (целое число) между датами today и birthday.

from datetime import date, timedelta

today = date(2021, 11, 4)
birthday = date(2022, 10, 6)

days = (birthday - today).days

print(days)
