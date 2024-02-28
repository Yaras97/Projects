def non_negative_even(numbers):
    return all(map(lambda x: True if x >= 0 and x % 2 == 0 else False, numbers))


# def non_negative_even(numbers):
#     return all(x % 2 == 0 and x >= 0 for x in numbers)

print(non_negative_even([0, 2, 4, 8, 16]))
print(non_negative_even([-8, -4, -2, 0, 2, 4, 8]))