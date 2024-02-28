def bee(n):
    if n < 5:
        bee(n + 1)
    else:
        print(n)

bee(0)