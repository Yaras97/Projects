def my_pow(number):
    return sum([int(n)**int(i) for i, n in enumerate(list(str(number)), 1)])


print(my_pow(139))