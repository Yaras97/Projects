import functools


def returns(datatype):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, datatype):
                return result
            else:
                raise TypeError
        return wrapper

    return decorator


@returns(int)
def add(a, b):
    return a + b

print(add(a=10, b=5))