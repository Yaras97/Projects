def outer():
    x = 'bee'

    def inner():
        x = 'geek'
        print(x)

    inner()
    print(x)


outer()
