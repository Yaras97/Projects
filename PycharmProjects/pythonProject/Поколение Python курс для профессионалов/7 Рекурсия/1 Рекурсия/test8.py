def bee(n):
    if n >= 7:
        print('bee')
    else:
        print(n)
        bee(n + 1)


bee(4)
