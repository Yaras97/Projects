def bee(n):
    if n > 0:
        bee(n - 1)
        print(n)

bee(3)