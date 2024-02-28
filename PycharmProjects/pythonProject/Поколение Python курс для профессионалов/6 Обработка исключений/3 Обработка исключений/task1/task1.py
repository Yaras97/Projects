import calendar

try:
    digit = int(input())
    (digit/digit)*digit
    months = list(calendar.month_name)
    print(months[digit])
except ValueError:
    print('Введено некорректное значение')
except (IndexError, ZeroDivisionError):
    print('Введено число из недопустимого диапазона')