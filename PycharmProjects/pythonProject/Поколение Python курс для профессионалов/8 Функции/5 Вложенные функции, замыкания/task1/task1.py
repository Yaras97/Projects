def power(degree):
    def num(x):
        return x ** degree

    return num


result = power(-2)(0.25)
print(result)