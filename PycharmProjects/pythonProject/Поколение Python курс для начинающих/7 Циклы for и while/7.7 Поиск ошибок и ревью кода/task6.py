n = int(input())
product = 1
while n:
    digit = n % 10
    product = product * digit
    n //= 10
print(product)