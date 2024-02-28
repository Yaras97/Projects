import functools
import time


def repeater(repeat):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, repeat + 1):
                print(f'{i}-ый запуск функции.')
                value = func(*args, **kwargs)
            return value

        return wrapper

    return decorator


def delayed(delay):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f'Спим {delay} сек.')
            time.sleep(delay)
            value = func(*args, **kwargs)
            return value

        return wrapper

    return decorator


def beegeek():
    return 'beegeek'


beegeek = repeater(3)(beegeek)
beegeek = delayed(1)(beegeek)


# beegeek = repeater(3, delayed(2, beegeek)) # НЕ правильно

# beegeek = repeater(3)(delayed(2)(beegeek))

beegeek()