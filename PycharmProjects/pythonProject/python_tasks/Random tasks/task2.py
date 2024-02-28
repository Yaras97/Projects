import time
print(time.strftime('Текущее время: %X'))
print('Задержка...')
time.sleep(5)
print('Прошло время.')
print(time.strftime('Текущее время: %X.'))


def longrunning_function():
    for i in range(3):
        time.sleep(1)


def shortrunning_function():
    n = 1
    for i in range(2, 100):
        n *= i


start = time.perf_counter()
longrunning_function()
end = time.perf_counter()
print("Выполнение longrunning_function() заняло {} c.".format(end - start))

start = time.perf_counter()
shortrunning_function()
end = time.perf_counter()
print("Выполнение shortrunning_function() заняло {} c.".format(end - start))


