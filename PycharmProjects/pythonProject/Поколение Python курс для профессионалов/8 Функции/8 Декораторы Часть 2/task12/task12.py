import functools


def ignore_exception(*d_args):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except d_args as err:

                return print(f'Исключение {err.__class__.__name__} обработано')

        return wrapper
    return decorator


min = ignore_exception(ZeroDivisionError)(min)

try:
    print(min(1, '2', 3, [4, 5]))
except Exception as e:
    print(type(e))