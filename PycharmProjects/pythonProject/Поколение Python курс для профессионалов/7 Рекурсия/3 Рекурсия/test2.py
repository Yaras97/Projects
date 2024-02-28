def f(n):
    if n in (1, 2, 3):
        return 1
    else:
        return 2*f(n - 1) + 4*f(n - 3) + f(n - 2)


print(f(6))