def my_func(a, b, *args, name='Gvido', age=17, **kwargs):
    print(a, b)
    print(*args)
    print(name, age)
    print(kwargs)

my_func(1, 2, 3, 4, name='Timur', age=28, job='Teacher', language='Python')
my_func(1, 2, name='Timur', age=28, job='Teacher', language='Python')
my_func(1, 2, 3, 4, job='Teacher', language='Python')