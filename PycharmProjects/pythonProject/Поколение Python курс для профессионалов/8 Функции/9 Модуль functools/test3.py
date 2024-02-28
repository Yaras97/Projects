from functools import partial, update_wrapper
def add(a, b):
    '''documentation'''
    return a + b
add_one = partial(add, 1)
update_wrapper(add_one, add)
print(add_one.__name__)
print(add_one.__doc__)