def make_upper(func):
    def wrapper():
        return func().upper()

    return wrapper


@make_upper
def beegeek():
    '''documentation'''
    return 'beegeek'


print(beegeek.__name__)
print(beegeek.__doc__)
