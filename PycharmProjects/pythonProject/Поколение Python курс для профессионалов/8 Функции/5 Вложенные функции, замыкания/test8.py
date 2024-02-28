def outer(x):
    def inner():
        return x

    x = None
    return inner


print(outer(10)())
