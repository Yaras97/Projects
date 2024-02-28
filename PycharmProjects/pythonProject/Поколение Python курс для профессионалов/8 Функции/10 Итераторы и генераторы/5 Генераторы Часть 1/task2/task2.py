def alternating_sequence(count=None):
    index = 1
    if count is None:
        while index:
            if index % 2 == 1:
                yield index
            if index % 2 == 0:
                yield -index
            index += 1
    else:
        for i in range(1, count + 1):
            if i % 2 == 1:
                yield i
            if i % 2 == 0:
                yield -i


generator = alternating_sequence(1)

try:
    print(next(generator))
    print(next(generator))
except StopIteration:
    print('Error')