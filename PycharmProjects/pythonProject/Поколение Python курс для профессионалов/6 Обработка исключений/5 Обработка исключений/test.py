class NegativeAgeError(Exception):
    pass


try:
    print('Введите свой возраст')
    age = int(input())
    if age < 0:
        raise NegativeAgeError('Возраст не может быть отрицательным')
    print('Ваш возраст равен', age)
except ValueError:
    print('Возраст должен быть числом')
except NegativeAgeError as e:
    print(e)
