def print_digits(number, c=0):
    if c < len(str(number)):
        print(list(str(number))[c])
        print_digits(number, c+1)


print_digits(8)