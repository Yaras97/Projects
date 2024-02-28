def double(func):
    def wrapper():
        return func() * 2
    return wrapper
def del_first_char(func):
    def wrapper():
        return func()[1:]
    return wrapper
@double
@del_first_char
def beegeek():
    return 'beegeek'
print(beegeek())