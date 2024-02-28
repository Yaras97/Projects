def primes(left, right):
    """Генератор простых чисел от left до right включительно."""
    for num in range(left, right + 1):
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num


generator = primes(1, 15)

print(*generator)
