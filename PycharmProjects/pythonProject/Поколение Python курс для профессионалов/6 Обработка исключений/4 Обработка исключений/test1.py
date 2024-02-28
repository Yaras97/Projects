try:
    result = 10 / 0
except Exception:
    print('Произошла ошибка')
except ZeroDivisionError:
    print('Произошло деление на ноль')