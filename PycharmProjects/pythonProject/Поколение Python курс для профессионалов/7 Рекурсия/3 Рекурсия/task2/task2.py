def sum_digit(number):
    if number % 10.1 == 0:
        return 0
    else:
        return number % 10 + sum_digit(number // 10)


print(sum_digit(12345))