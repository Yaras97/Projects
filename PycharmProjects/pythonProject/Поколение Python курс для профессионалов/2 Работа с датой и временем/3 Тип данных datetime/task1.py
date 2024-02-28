from datetime import datetime
birthday = datetime(1992, 10, 6, 9, 48, 17)
a = birthday.replace(year=9999, month=11)
birthday.replace(year=9999, month=11)
print(birthday)
print(a)