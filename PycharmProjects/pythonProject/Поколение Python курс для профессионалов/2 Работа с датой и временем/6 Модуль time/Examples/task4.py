import time

start_time = time.monotonic()
for i in range(5):
    print(i)
    time.sleep(0.5)
end_time = time.monotonic()
elapsed_time = end_time - start_time
print(f'Время работы программы = {elapsed_time}')