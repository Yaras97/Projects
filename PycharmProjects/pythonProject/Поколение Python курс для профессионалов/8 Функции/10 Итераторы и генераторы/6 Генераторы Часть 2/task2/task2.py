def is_prime(number):
    return all(number % i != 0 for i in range(2, int(number**0.5) + 1)) and number > 1


print(is_prime(9973))