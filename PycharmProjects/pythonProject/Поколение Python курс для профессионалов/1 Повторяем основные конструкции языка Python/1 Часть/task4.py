def print_given(*args, **kwargs):
    for i in args:
        print(i, type(i))
    for name, value in sorted(kwargs.items()):
        print(name, value, type(value))


print_given(1, [1, 2, 3], 'three', two=2)


# def print_given(*args, **kwargs):
#     print(*(f'{i} {type(i)}' for i in args), sep='\n')
#     print(*(f'{k} {v} {type(v)}' for k, v in sorted(kwargs.items())), sep='\n')


# def print_given(*args, **kwargs):
#
#     for i in args:
#         print(i, type(i))
#     for j in sorted(kwargs):
#         print(j, kwargs[j], type(kwargs[j]))


# def print_given(*args, **kwargs):
#     [print(a, type(a)) for a in args]
#     [print(k, v, type(v)) for k, v in sorted(kwargs.items())]