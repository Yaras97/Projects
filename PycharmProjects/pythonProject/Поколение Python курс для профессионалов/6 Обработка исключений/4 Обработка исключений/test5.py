try:
    raise ValueError('oops', 'something went wrong')
except ValueError as e:
    print(e)
    print(e.args)