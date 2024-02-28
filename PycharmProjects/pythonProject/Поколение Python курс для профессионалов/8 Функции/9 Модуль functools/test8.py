from functools import lru_cache


@lru_cache()
def add_one(number):
    print(number + 1, end=' ')


numbers = [1, 2, 3, 1, 3, 4, 4, 1]
for i in numbers:
    add_one(i)

print(add_one.cache_info())