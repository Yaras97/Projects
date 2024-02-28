import functools


def takes(*values):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for i in args:
                if isinstance(i, values):
                    continue
                else:
                    raise TypeError
            for i in kwargs.values():
                if isinstance(i, values):
                    continue
                else:
                    raise TypeError
            return result

        return wrapper

    return decorator


@takes(str)
def beegeek(word, repeat):
    return word * repeat


try:
    print(beegeek('beegeek', repeat=2))
except TypeError as e:
    print(type(e))
