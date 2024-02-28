def outer(x):
    y = 20

    def inner(z):
        t = 30
        return x + y + z + t

    return inner


func = outer(10)
for var in func.__closure__:
    print(var.cell_contents)
