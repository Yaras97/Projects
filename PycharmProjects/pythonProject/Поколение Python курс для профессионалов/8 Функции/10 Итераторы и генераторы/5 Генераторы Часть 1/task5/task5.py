from datetime import date, timedelta


def dates(start, count=None):
    index = -1
    if count is None:
        while True:
            index += 1
            yield start + timedelta(days=index)

    else:
        for _ in range(count):
            index += 1
            yield start + timedelta(days=index)




generator = dates(date(9999, 1, 7))

for _ in range(348):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

try:
    print(next(generator))
except StopIteration:
    print('Error')