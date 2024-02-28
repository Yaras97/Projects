import functools


def strip_range(start, end, char='.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            len_sym = end - start
            if start in range(len(result) + 1):
                if len_sym > len(result):
                    len_sym = len_sym % len(result) + 1

                func_str = ''.join([char for _ in range(len_sym)])
                return result[:start] + func_str + result[end:]
            else:
                return result
        return wrapper

    return decorator


@strip_range(0, 1)
def beegeek(word, end=" "):
    """This is... Requiem. What you are seeing is indeed the truth"""
    return word + end

print(beegeek("beegee", end="k"))
print(beegeek.__name__)
print(beegeek.__doc__)