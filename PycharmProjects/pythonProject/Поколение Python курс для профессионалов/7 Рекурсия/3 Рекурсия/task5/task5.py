def get_pow(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    return a * get_pow(a, n - 1)


print(get_pow(10, 4))
