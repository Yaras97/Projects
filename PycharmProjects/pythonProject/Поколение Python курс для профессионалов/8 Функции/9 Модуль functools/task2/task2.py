import time, sys
from functools import lru_cache

start = time.perf_counter()


@lru_cache(typed=False)
def alphabet(value):
    return ''.join(sorted(value))


message = [i.strip() for i in sys.stdin]

for word in message:
    result = alphabet(word)
    print(result)

end = time.perf_counter()
work_time = end - start
print(f'Время выполнения {round(work_time, 4)} сек.')
