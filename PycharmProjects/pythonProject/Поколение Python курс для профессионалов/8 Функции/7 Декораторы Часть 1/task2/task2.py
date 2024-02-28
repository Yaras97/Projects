# def print(*args, sep=' ', end='\n', file=None, flush=False):
#     args = [str(arg).upper() for arg in args]
#     sep = str(sep).upper()
#     end = str(end).upper()
#
#     __builtins__.print(*args, sep=sep, end=end)


def uppercase_decorator(func):
    def wrapper(*args, sep=' ', end='\n', file=None, flush=False):
        args = [str(arg).upper() for arg in args]
        sep = str(sep).upper()
        end = str(end).upper()

        func(*args, sep=sep, end=end)

    return wrapper


# Переопределение функции print с использованием декоратора
print = uppercase_decorator(print)

print('aaa', 'bbb', 'CCC', sep='xxx', end='stepik')
print('aaa', 'bbb', 'CCC', sep='--', end='python')
print('aaa', 'bbb', 'CCC', sep='qqq', end='!')
