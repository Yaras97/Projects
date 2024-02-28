def print(*args, sep=' ', end='\n', file=None):
    modified_args = [str(arg).upper() for arg in args]
    modified_sep = str(sep).upper()
    modified_end = str(end).upper()

    built_output = modified_sep.join(modified_args) + modified_end
    built_output += '\n' if modified_end == '\n' else ''  # Добавляем новую строку, если end = '\n'

    __builtins__.print(built_output, sep='', end='', file=file)




# print('beegeek', [1, 2, 3], 4)
print('bee', 'geek', sep=' and ', end=' wow')
print(help(__builtins__))