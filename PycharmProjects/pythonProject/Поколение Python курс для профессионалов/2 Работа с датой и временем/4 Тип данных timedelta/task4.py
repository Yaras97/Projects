from datetime import datetime, timedelta
day = datetime.strptime(input(), '%H:%M:%S')
n = int(input())
print(datetime.strftime(day + timedelta(seconds=n), '%H:%M:%S'))