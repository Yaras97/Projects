def bee(n):
    if n < 5:
        print(n)
    else:
        bee(n + 1)

bee(0)