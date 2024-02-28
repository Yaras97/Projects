from datetime import date, time


def is_correct(day, month, year):
    try:
        if date(year, month, day):
            return True
    except ValueError:
        return False


count = 0
x_date = input()

while x_date != 'end':
    day, month, year = x_date.split('.')
    if is_correct(int(day), int(month), int(year)):
        count += 1
        print('Корректная')
    else:
        print('Некорректная')
    x_date = input()
print(count)