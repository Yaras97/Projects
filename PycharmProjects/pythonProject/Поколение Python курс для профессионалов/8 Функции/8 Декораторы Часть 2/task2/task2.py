import functools

def returns_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not isinstance(func(*args, **kwargs), str):
            raise TypeError

        return func(*args, **kwargs)

    return wrapper


@returns_string
def concat(*args, **kwargs):
    return "".join([*args, *kwargs.values()])

print(concat("Hello ", x="world", y="!!!"))
