def make_lower(func):
    def wrapper():
        return func().lower()

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper


@make_lower
def beegeek():
    '''documentation'''
    return 'beegeek'


print(beegeek.__name__)
print(beegeek.__doc__)
