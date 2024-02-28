def to_binary(number):
    if number == 1:
        return '1'
    if number == 0:
        return '0'
    return to_binary(number // 2) + str(number % 2)


print(to_binary(10))
print(to_binary(25))
print(to_binary(2))
print(to_binary(0))