
from functools import wraps

def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ', '.join(map(repr, args))
        kwargs_str = ', '.join([f'{key}={value}' for key, value in kwargs.items()])
        all_args_str = f'({args_str})' + (f', {kwargs_str}' if kwargs_str else '')

        print(f"TRACE: вызов {func.__name__} с аргументами: {all_args_str}")
        result = func(*args, **kwargs)
        print(f"TRACE: возвращаемое значение {func.__name__}: {repr(result)}")

        return result

    return wrapper


@trace
def sub(a, b, c):
    '''прекрасная функция'''
    return a - b + c


print(sub.__name__)
print(sub.__doc__)
sub(20, 5, c=10)