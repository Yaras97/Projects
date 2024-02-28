def palindromes():
    count = 0
    while True:
        count += 1
        if str(count) == str(count)[::-1]:
            yield count


generator = palindromes()

for _ in range(100):
    print(next(generator))