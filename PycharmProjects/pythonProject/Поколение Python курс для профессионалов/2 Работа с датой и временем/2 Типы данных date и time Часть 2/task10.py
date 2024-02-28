from datetime import date, time


def is_correct(day, month, year):
    try:
        if date(year, month, day):
            return True
    except ValueError:
        return False


print(is_correct(31, 12, 2021))
print(is_correct(31, 13, 2021))
print(is_correct(32, 10, 2021))
print(is_correct(99, 99, 2021))


# from datetime import date, time
#
#
# def is_correct(day, month, year):
#     try:
#         date1 = date(year, month, day)
#         return True
#     except:
#         return False