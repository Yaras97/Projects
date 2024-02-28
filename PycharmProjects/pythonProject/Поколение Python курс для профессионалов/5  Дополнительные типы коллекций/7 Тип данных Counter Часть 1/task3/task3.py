from collections import Counter

products = Counter(sorted(input().split(',')))
[print(f'{i}: {products[i]}') for i in products]
