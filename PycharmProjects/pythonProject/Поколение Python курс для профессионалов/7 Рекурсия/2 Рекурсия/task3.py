numbers = [i for i in range(200, 301)]


def count(n, c=0):
    if c < len(n):
        print(f'Элемент {c}: {n[c]}')
        count(n, c + 1)


count(numbers)