from datetime import date


def get_min_max(dates):
    if dates:
        return min(dates), max(dates)
    return ()


a = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]
print(get_min_max(a))



# from datetime import date
#
#
# def get_min_max(lst):
#     return (min(lst), max(lst)) if lst else ()


# from datetime import date
#
# def get_min_max(dates):
#     return tuple(dates) and (min(dates), max(dates))