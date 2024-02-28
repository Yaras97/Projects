import functools


def add_attrs(**dec_kwargs):
    def decorator(func):
        for key, value in dec_kwargs.items():
            func.__dict__[key] = value

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@add_attrs(func_attr='i am attribute')
def func(a, b):
    '''func docs'''
    return


print(func.func_attr)