def make_upper(func):
    def wrapper():
        return func().upper()

    return wrapper


def beegeek():
    return 'beegeek'


new_beegeek = make_upper(beegeek)
print(beegeek())
print(new_beegeek())
