import calendar
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


def get_weekday(number):
    try:
        (list(' ') + list(calendar.day_name))[number].capitalize()
        if int(number) < 1 or int(number) > 7:
            raise ValueError('Аргумент не принадлежит требуемому диапазону')
        if not str(number).isdigit():
            raise TypeError('Аргумент не является целым числом')

    except ValueError as arr:
        raise ValueError('Аргумент не принадлежит требуемому диапазону') from arr
    except TypeError as arr:
        raise TypeError('Аргумент не является целым числом') from arr
    except IndexError as arr:
        raise ValueError('Аргумент не принадлежит требуемому диапазону') from arr
    except Exception as arr:
        raise TypeError('Аргумент не является целым числом') from arr
    else:
        return (list(' ') + list(calendar.day_name))[number].capitalize()


try:
    print(get_weekday(set()))
except Exception as err:
    print(err)
    print(type(err))