# пустая строка в списке соответствует нулевому месяцу, первый месяц - январь
import calendar
month_names = ['', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь',
               'ноябрь', 'декабрь']
calendar.month_name = month_names
print(calendar.prmonth(2019, 12))


calendar.month_name = calendar.month_abbr
print(calendar.prmonth(1985, 10))