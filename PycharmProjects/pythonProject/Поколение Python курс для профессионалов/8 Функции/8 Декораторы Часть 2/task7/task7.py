import functools


def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times - 1):
                func(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper
    return decorator


counter = 0


@repeat(5)
def say(word):
    print(word)

say(word="Hey!")