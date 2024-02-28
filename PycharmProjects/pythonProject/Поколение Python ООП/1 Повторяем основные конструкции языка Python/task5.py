import json
import functools

def jsonify(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        value = json.dumps(func(*args, **kwargs))
        return value
    return wrapper


@jsonify
def make_tuple():
    """JSON-Tuple object"""
    return (1, '2', 3.0, None, False, {'1': True})


print(make_tuple())
print(make_tuple.__name__)
print(make_tuple.__doc__)