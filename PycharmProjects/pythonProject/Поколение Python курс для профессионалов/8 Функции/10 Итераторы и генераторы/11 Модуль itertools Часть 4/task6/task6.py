from itertools import groupby

def ranges(numbers):
    result = []
    for key, group in groupby(enumerate(numbers), lambda x: x[1] - x[0]):
        group = list(group)
        result.append((group[0][1], group[-1][1]))

    return result


numbers = [1, 2, 3, 4, 7, 8, 10]

print(ranges(numbers))


