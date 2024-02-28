def simple_sequence():
    counter = 1
    while counter:
        for _ in range(counter):
            yield counter
        counter += 1


generator = simple_sequence()

for _ in range(100):
    print(next(generator))