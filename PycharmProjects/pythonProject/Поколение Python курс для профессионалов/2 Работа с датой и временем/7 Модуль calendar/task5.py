import calendar, datetime


def get_days_in_month(year, month):
    month_dict = {'': 0, 'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7,
                  'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
    amount_days = calendar.monthrange(year, month_dict[month])[1]
    list_days = []
    for i in range(1, amount_days + 1):
        list_days.append(datetime.date(year, month_dict[month], i))
    print(list_days)


get_days_in_month(2021, 'December')