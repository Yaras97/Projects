from fractions import Fraction as F
n = input()
m = input()
a = F(n)
b = F(m)
print(n, '+', m, '=', a + b)
print(n, '-', m, '=', a - b)
print(n, '*', m, '=', a * b)
print(n, '/', m, '=', a / b)