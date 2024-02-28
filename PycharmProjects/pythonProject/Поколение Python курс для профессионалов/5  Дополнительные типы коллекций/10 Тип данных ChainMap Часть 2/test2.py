from collections import ChainMap

fruits = ChainMap({'apple': 10, 'banana': 20},
                  {'lemon': 10, 'pineapple': 15},
                  {'kiwi': 15, 'lime': 5})
fruits.maps.append({'mango': 20, 'melon': 20})

del fruits.maps[0]
del fruits.maps[1]

print(fruits)

