from datetime import date, time, datetime
dt = datetime.combine(date(2022, 6, 10), time(13, 50, 59))
print(dt.day + dt.second)