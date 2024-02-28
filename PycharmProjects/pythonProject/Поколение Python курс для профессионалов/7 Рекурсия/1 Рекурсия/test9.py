def bee(n):
    if n >= 7:
        print('bee')
    else:
        bee(n + 1)
        print(n)


bee(4)