import functools


def make_html(tag):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return '<' + tag + '>' + func(*args, **kwargs) + '<' + '/' + tag + '>'

        return wrapper

    return decorator


@make_html('mark')
@make_html('mark')
@make_html('mark')
def beegeek():
    '''beegeek docs'''
    return 'beegeek'


print(beegeek())
print(beegeek.__name__)
print(beegeek.__doc__)