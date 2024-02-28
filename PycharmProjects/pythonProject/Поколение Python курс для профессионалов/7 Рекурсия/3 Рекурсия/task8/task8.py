def is_power(number):
    if number == 1:
        return True
    if number % 2 != 0:
        return False
    return is_power(number // 2)


print(is_power(1024))