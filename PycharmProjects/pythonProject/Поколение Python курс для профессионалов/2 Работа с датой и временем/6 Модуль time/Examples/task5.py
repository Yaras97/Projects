import time

start_time = time.perf_counter()
for i in range(5):
    print(i)
    time.sleep(1)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f'Время работы программы = {elapsed_time}')