def closure():
    count = 0

    def inner():
        nonlocal count
        count += 1
        print(count)
    return inner


start = closure()
another = closure()  # another instance, with a different stack
start()  # prints 1
start()  # prints 2
another()  # print 1
start()  # prints 3
