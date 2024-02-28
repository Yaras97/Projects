from datetime import date
import calendar, datetime


def get_days_in_month(year):
    list_days = []
    for j in range(1, 13):
        amount_days = calendar.monthrange(year, j)[1]
        for i in range(1, amount_days + 1):
            if date(year, j, i).isoweekday() == 1:
                list_days.append(datetime.date(year, j, i))

    print(list_days)


get_days_in_month(2023)
