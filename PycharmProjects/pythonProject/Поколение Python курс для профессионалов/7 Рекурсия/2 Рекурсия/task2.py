def count_100(n):
    if n < 101:
        print(n)
        count_100(n + 1)


count_100(1)