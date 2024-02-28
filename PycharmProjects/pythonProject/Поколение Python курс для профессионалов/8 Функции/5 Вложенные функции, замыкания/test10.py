def make_counter(i):
    def counter():
        nonlocal i
        i += 1
        return i

    return counter


counter1 = make_counter(100)
counter2 = make_counter(200)
print(counter1(), counter1())
print(counter2(), counter2())
