def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper


@do_twice
def beegeek(*args, **kwargs):
    print('beegeek' * sum(args + tuple(kwargs.values())))


beegeek(1, 1, 1, sep=1, end=2, step=3)
