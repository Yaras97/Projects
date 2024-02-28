from datetime import date, timedelta

def dates(start, count=None):
    """Генератор дат, начиная с даты start."""
    current_date = start
    days_to_generate = count

    while days_to_generate is None or days_to_generate > 0:
        yield current_date
        current_date += timedelta(days=1)

        if days_to_generate is not None:
            days_to_generate -= 1


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