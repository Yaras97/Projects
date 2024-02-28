n = int(input())
langs = set(input().split(', '))

for i in range(n - 1):
    langs &= set(input().split(', '))

if langs:
    print(*sorted(langs), sep=', ')

else:
    print('Сериал снять не удастся')



