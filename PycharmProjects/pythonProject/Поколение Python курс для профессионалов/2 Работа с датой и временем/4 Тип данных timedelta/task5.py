from datetime import datetime


def num_of_sundays(year):
    d = datetime(year, 12, 31)
    return d.strftime('%U')


print(num_of_sundays(2021))
year = 2000
print(num_of_sundays(year))
print(num_of_sundays(768))