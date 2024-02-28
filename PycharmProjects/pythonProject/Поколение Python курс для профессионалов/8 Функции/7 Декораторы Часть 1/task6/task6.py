def takes_positive(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError
            if arg <= 0:
                raise ValueError
        for kw in kwargs.values():
            if not isinstance(kw, int):
                raise TypeError
            if kw <= 0:
                raise ValueError
        return func(*args, **kwargs)

    return wrapper


@takes_positive
def power(a, n):
    return a ** n


try:
    print(power(a="3", n="2"))
except Exception as err:
    print(type(err))