from collections import ChainMap
fruits = ChainMap({'apple': 1, 'banana': 25},
{'lemon': 10, 'pineapple': 20},
{'kiwi': 15, 'lime': 5})
print(*fruits.values())