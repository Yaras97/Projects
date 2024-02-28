from datetime import datetime
datetimes = [datetime(2022, 6, 11, 13, 26),
datetime(2000, 12, 31, 23, 59),
datetime(2077, 1, 1, 12),
datetime(2042, 7, 29)]
print(min(datetimes, key=lambda dt: dt.hour))
print(max(datetimes, key=lambda dt: dt.year))