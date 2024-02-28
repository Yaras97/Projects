from datetime import datetime
a = []
dates = input().split()
for i in range(1, len(dates)):
    d = (datetime.strptime(dates[i], '%d.%m.%Y') - datetime.strptime(dates[i - 1], '%d.%m.%Y')).days
    a.append(abs(d))
print(a)


# from datetime import datetime, timedelta
#
# dates = [datetime.strptime(x, '%d.%m.%Y') for x in input().split()]
#
# difference = [abs(dates[i] - dates[i + 1]).days for i in range(len(dates) - 1)]
#
# print(difference)