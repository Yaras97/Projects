def convert(number):
    if number >= 0:
        return bin(number)[2:], oct(number)[2:], hex(number)[2:]
    else:
        return '-' + bin(number)[3:], '-' + oct(number)[3:], '-' + hex(number)[3:]


print(convert(-0))
print(convert(1))