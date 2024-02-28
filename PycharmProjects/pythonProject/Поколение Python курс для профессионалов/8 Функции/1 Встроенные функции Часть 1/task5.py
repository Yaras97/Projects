def is_greater(lists, number):
    return any(sum(i) > number for i in lists)


data = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
print(is_greater(data, 2))