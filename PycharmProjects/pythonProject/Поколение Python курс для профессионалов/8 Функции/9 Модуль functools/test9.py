from functools import lru_cache


@lru_cache()
def average(numbers):
    return sum(numbers) / len(numbers)


numbers = [1, 2, 3, 4, 5]

print(average(numbers))
print(average(numbers))
