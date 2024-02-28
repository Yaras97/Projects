import sys
import time
from functools import lru_cache


@lru_cache(maxsize=None)
def lex_order(word):
    return ''.join(sorted(word))


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed Time: {elapsed_time:.6f} seconds")
        return result

    return wrapper


# @timing_decorator
# def main():
#     # Чтение входных данных
#     words = [line.strip() for line in sys.stdin]
#
#     # Обработка и вывод результатов
#     for word in words:
#         result = lex_order(word)
#         print(result)
#
#
# if __name__ == "__main__":
#     main()
