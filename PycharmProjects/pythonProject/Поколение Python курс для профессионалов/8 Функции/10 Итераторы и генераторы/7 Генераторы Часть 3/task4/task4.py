from datetime import date, timedelta

def years_days(year):
    start_date = date(year, 1, 1)
    end_date = date(year, 12, 31)
    current_date = start_date

    while current_date <= end_date:
        yield current_date
        current_date += timedelta(days=1)


dates = years_days(1900)

print(*dates)