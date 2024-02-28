import functools


def ignore_exception(*exception_types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_types as e:
                print(f'Исключение {type(e).__name__} обработано')

        return wrapper

    return decorator


@ignore_exception(ValueError, TypeError, NameError)
def func():
    '''func docs'''
    raise ValueError


print(func.__name__)
print(func.__doc__)

try:
    func()
except Exception as e:
    print(type(e))
