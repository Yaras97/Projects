def make_lower(func):
    def wrapper():
        return func().lower()

    return wrapper


def make_capitalize(func):
    def wrapper():
        return func().capitalize()

    return wrapper


def beegeek():
    return 'BEEGEEK'


beegeek = make_lower(make_capitalize(beegeek))
print(beegeek())
