try:
    raise ValueError('oops')
except ValueError as e:
    print(e)
    print(e.args)
    print(type(e.args))