def generator_square_polynom(a, b, c):
    def equation(x):
        return a*x**2 + b*x + c
    return equation

print(generator_square_polynom(26.17, 83.33, 22.3)(-1))