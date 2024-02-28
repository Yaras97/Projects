try:
    result = 10 / 0
except Exception:
    print('Произошла ошибка 1')
except:
    print('Произошла ошибка 2')