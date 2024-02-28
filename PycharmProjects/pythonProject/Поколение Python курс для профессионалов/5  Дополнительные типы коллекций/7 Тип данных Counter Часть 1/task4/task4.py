from collections import Counter

products = Counter(sorted(input().split(',')))
max_word = max(map(len, products))
for prod in products:
    price = sum([int(ord(letter)) for letter in prod])
    print(f'{prod:<{max_word}}: {price} x {products[prod]} = {price * products[prod]} UC')
