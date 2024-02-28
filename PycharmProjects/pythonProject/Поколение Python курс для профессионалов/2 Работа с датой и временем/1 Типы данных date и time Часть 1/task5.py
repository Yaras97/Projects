from datetime import date

dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11), date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21), date(1666, 6, 6), date(1968, 5, 26)]
for i in dates:
    if i.month in [1, 2, 3]:
        print(f'{i.year}-Q1')
    elif i.month in [4, 5, 6]:
        print(f'{i.year}-Q2')
    elif i.month in [7, 8, 9]:
        print(f'{i.year}-Q3')
    elif i.month in [10, 11, 12]:
        print(f'{i.year}-Q4')



# from datetime import date
#
# dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11), date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21), date(1666, 6, 6), date(1968, 5, 26)]
#
# for d in dates:
#     print(f'{d.year}-Q{(d.month - 1) // 3 + 1}')


# from datetime import date
#
# dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11), date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21), date(1666, 6, 6), date(1968, 5, 26)]
# for date in dates:
#     print(f'{date.year}-Q{"111222333444"[date.month-1]}')