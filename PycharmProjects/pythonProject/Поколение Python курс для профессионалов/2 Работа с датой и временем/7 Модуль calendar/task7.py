from datetime import date
import calendar, datetime


def third_thursday_in_month(year):
    list_days = {}
    thursdays = []
    for j in range(1, 13):
        amount_days = calendar.monthrange(year, j)[1]
        list_days[j] = list()
        for i in range(1, amount_days + 1):
            if date(year, j, i).isoweekday() == 4:
                list_days[j].append(datetime.date(year, j, i).strftime('%Y.%m.%d'))
        thursdays.append(list_days[j][2])

    print(*thursdays, sep='\n')


third_thursday_in_month(2023)
