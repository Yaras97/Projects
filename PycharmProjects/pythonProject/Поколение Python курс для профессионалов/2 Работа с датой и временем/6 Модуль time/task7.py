def list_function(iterable):    # с использованием встроенной функции list()
    return list(iterable)


print(list_function(range(100_000)))
