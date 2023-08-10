"""
from math import *
n = int(input())
summ = 0
for i in range(1, n + 1):
    summ += factorial(i)
print(summ)
"""

from math import *
n = int(input())
summ = 0
fac = 0
while n:
    fac = factorial(n)
    summ += fac
    n -= 1
print(summ)