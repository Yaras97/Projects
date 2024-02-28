def outer():
    x = 'bee'

    def inner():
        nonlocal x
        x = 'geek'
        print(x)

    inner()
    print(x)


outer()
