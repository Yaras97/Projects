from datetime import datetime, timedelta


def fill_up_missing_dates(dates):
    pattern = '%d.%m.%Y'
    dates = [datetime.strptime(x, pattern) for x in dates]
    start, finish = min(dates), max(dates)
    days = (finish - start).days + 1
    return [(start + timedelta(days=i)).strftime(pattern) for i in range(days)]


dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
print(fill_up_missing_dates(dates))


dates = ['01.11.2021', '04.11.2021', '09.11.2021', '15.11.2021']
print(fill_up_missing_dates(dates))