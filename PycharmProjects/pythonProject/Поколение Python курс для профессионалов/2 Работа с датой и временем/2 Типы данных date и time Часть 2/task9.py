from datetime import date


def print_good_dates(lst):
    for i in sorted(filter(lambda x: x.year == 1992 and x.month + x.day == 29, lst)):
        print(i.strftime('%B %d, %Y'))


dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)