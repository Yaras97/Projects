def digit(number):
    if not number % 10.1:
        return 0
    else:
        return 1 + digit(number // 10)


print(digit(101001000245))