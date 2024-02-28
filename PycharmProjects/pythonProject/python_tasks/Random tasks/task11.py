import time
local_time = time.ctime() # вызов функции без аргумента
print('Местное время:', local_time)


seconds = time.time()
local_time = time.ctime(seconds)
print('Местное время:', local_time)