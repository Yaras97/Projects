import time


def sleep_function():
    for i in range(1, 11):
        time.sleep(i)
    print('Hello World!')


start = time.perf_counter()
sleep_function()
end = time.perf_counter()
print("Выполнение sleep_function() заняло {} c.".format(end - start))