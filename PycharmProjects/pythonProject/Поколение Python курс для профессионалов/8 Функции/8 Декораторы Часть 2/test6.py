def make_upper(func):
    def wrapper():
        return func().upper()

    return wrapper


def del_first_char(func):
    def wrapper():
        return func()[1:]

    return wrapper


def reverse(func):
    def wrapper():
        return func()[::-1]

    return wrapper


@reverse
@del_first_char
@make_upper
def beegeek():
    return 'beegeek'


print(beegeek())
