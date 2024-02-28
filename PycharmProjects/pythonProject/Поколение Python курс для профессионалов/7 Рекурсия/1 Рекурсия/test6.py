def beegeek(n):
    if n > 0:
        print('bee')
        beegeek(n - 1)
    else:
        print('geek')

beegeek(3)