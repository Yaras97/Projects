import time


def add(a, b, c):
    time.sleep(3)
    return a + b + c


def calculate_it(func, *args):
    start_time = time.perf_counter()
    func(*args)
    end_time = time.perf_counter()
    difference_time = end_time - start_time
    return func(*args), difference_time


print(calculate_it(add, 1, 2, 3))
