def my_func(**kwargs):
    print(type(kwargs))
    print(kwargs)

info = {'name':'Timur', 'age':'28', 'job':'teacher'}

my_func(info)