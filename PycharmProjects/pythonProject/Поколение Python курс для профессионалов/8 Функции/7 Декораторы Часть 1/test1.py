def bold(func):
    def wrapper():
        return '<b>' + func() + '</b>'

    return wrapper


def italic(func):
    def wrapper():
        return '<i>' + func() + '</i>'

    return wrapper

# @bold
# @italic
def greet():
    return 'Hello world!'


# greet = bold(italic(greet))
greet = italic(greet)
greet = bold(greet)
print(greet())